import json
import zipfile
import io
import os
import tempfile
import uuid

from os.path import abspath

from configuration.config import Config

from utils.logger import LoggingService
from utils.s3 import S3Service
from utils.sql import SqlService
from utils.file import FileManipulator

logger = LoggingService(name="main").logger


def lambda_handler(event, context):
    try:
        for record in event.get("Records", []):
            message_records = json.loads(record.get("body"))["Records"]

            for message_record in message_records:
                # Recupera bucket e key do evento S3
                try:
                    bucket = message_record["s3"].get("bucket").get("name")
                    key = message_record["s3"].get("object").get("key")
                    extraction_date = key.split("/")[0]
                    logger.info(f"Arquivo {key} encontrado no bucket {bucket}")
                except Exception as e:
                    logger.error(f"Erro ao extrair informações do evento S3: {e}")

                # Leitura do arquivo zip
                logger.info(f"Processando arquivo {key} do bucket {bucket}")
                response = S3Service(bucket_name=bucket, object_name=key).get_object()

                # Descompacta o arquivo zip
                with zipfile.ZipFile(io.BytesIO(response), "r") as zip_file:
                    for file_name in zip_file.namelist():
                        if not file_name.endswith(".txt"):
                            continue

                        tmp_dir = tempfile.gettempdir()
                        txt_path = os.path.join(tmp_dir, file_name)

                        FileManipulator().write_temp_file(file_name, zip_file, txt_path)

                        sql_path = abspath(
                            f"src/transformation/utils/schema/{file_name.replace('.txt', '.sql')}"
                        )

                        # Formata e lê a query SQL
                        logger.info(f"Formatando e executando query SQL para o arquivo {file_name}")
                        query = SqlService().format_query(
                            sql_path, txt_path=txt_path, extraction_date=extraction_date
                        )
                        df = SqlService().execute_query(query)

                        logger.info("Gravando arquivo no S3")
                        new_file_name = (
                            FileManipulator()
                            .file_name_mapping()
                            .get(file_name, file_name.replace(".txt", ""))
                        )
                        bucket_processed = Config.BUCKET_NAME_PROCESSED
                        object_name = (
                            f"{new_file_name}/{extraction_date}/{uuid.uuid4()}.parquet"
                        )

                        S3Service(bucket_processed, object_name).put_object(
                            df.to_parquet(
                                index=False, engine="pyarrow", compression="snappy"
                            )
                        )
                        logger.info(
                            f"Arquivo {object_name} enviado para o bucket {bucket_processed} com sucesso"
                        )

    except Exception as e:
        logger.error(f"Erro ao processar o evento: {e}")
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}


if __name__ == "__main__":
    event = {
        "Records": [
            {
                "messageId": "c6f29b8f-7b5e-4d39-9399-0e3f1c59aeb2",
                "receiptHandle": "AQEB...long-receipt-handle...",
                "body": '{ "Records": [ { "eventVersion": "2.1", "eventSource": "aws:s3", "awsRegion": "us-east-1", "eventTime": "2025-03-30T12:34:56.789Z", "eventName": "ObjectCreated:Put", "s3": { "s3SchemaVersion": "1.0", "configurationId": "trigger-config-id", "bucket": { "name": "public-transit-data-raw", "ownerIdentity": { "principalId": "A1B2C3D4E5F6G7" }, "arn": "arn:aws:s3:::public-transit-data-raw" }, "object": { "key": "2025-03-30/sp_trans_data_11_13_41.zip", "size": 10485760, "eTag": "d41d8cd98f00b204e9800998ecf8427e", "sequencer": "0055AED6DCD90281E5" } } } ] }',
                "attributes": {
                    "ApproximateReceiveCount": "1",
                    "SentTimestamp": "1711791296789",
                    "SenderId": "AIDAIOSFODNN7EXAMPLE",
                    "ApproximateFirstReceiveTimestamp": "1711791299999",
                },
                "messageAttributes": {},
                "md5OfBody": "e99a18c428cb38d5f260853678922e03",
                "eventSource": "aws:sqs",
                "eventSourceARN": "arn:aws:sqs:us-east-1:123456789012:public-transit-data-sqs-queue",
                "awsRegion": "us-east-1",
            }
        ]
    }

    lambda_handler(event=event, context={})
