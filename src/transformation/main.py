import json

def lambda_handler(event, context):
    """
    Função principal da AWS Lambda para processar eventos do SQS.
    """
    try:
        for record in event.get('Records', []):
            message_records = json.loads(record.get('body'))['Records']

            for message_record in message_records:
                bucket = message_record['s3'].get('bucket').get('name')
                key = message_record['s3'].get('object').get('key')
                print(f"Arquivo {key} encontrado no bucket {bucket}")
            

            
            
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Mensagens processadas com sucesso!"})
        }
    except Exception as e:
        print(f"Erro ao processar o evento: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

if __name__ == "__main__":
    event = {"Records": [
        {
        "messageId": "c6f29b8f-7b5e-4d39-9399-0e3f1c59aeb2",
        "receiptHandle": "AQEB...long-receipt-handle...",
        "body": "{ \"Records\": [ { \"eventVersion\": \"2.1\", \"eventSource\": \"aws:s3\", \"awsRegion\": \"us-east-1\", \"eventTime\": \"2025-03-30T12:34:56.789Z\", \"eventName\": \"ObjectCreated:Put\", \"s3\": { \"s3SchemaVersion\": \"1.0\", \"configurationId\": \"trigger-config-id\", \"bucket\": { \"name\": \"public-transit-data-raw\", \"ownerIdentity\": { \"principalId\": \"A1B2C3D4E5F6G7\" }, \"arn\": \"arn:aws:s3:::public-transit-data-raw\" }, \"object\": { \"key\": \"2025-03-30/sp_trans_data_11_13_41.zip\", \"size\": 10485760, \"eTag\": \"d41d8cd98f00b204e9800998ecf8427e\", \"sequencer\": \"0055AED6DCD90281E5\" } } } ] }",
        "attributes": {
            "ApproximateReceiveCount": "1",
            "SentTimestamp": "1711791296789",
            "SenderId": "AIDAIOSFODNN7EXAMPLE",
            "ApproximateFirstReceiveTimestamp": "1711791299999"
        },
        "messageAttributes": {},
        "md5OfBody": "e99a18c428cb38d5f260853678922e03",
        "eventSource": "aws:sqs",
        "eventSourceARN": "arn:aws:sqs:us-east-1:123456789012:public-transit-data-sqs-queue",
        "awsRegion": "us-east-1"
        }
    ]
    }

    lambda_handler(event=event, context={})