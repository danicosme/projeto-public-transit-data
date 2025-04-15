import boto3

from logger import LoggingService

s3_client = boto3.client('s3')

class S3Service:
    def __init__(self, bucket_name: str, object_name: str):
        self.logger = LoggingService(name="S3Service").logger
        self.bucket_name = bucket_name
        self.object_name = object_name

    def put_object(self, data):
        """Faz o upload de um objeto para o bucket S3."""
        try:
            s3_client.put_object(
                Bucket=self.bucket_name,
                Key=self.object_name,
                Body=data
            )
        except Exception as e:
            self.logger.error(f"Erro ao gravar arquivo no S3 (Bucket: {self.bucket_name}, Objeto: {self.object_name}): {e}")
            raise