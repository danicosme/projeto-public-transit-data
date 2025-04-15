import boto3

from utils.logger import LoggingService

s3_client = boto3.client('s3')

class S3Service:
    def __init__(self, bucket_name: str, object_name: str):
        self.logger = LoggingService(name="S3Service").logger
        self.bucket_name = bucket_name
        self.object_name = object_name
    
    def get_object(self):
        try:
            return s3_client.get_object(Bucket=self.bucket_name,
                                Key=self.object_name)['Body'].read()
        except Exception as e:
            self.logger.error(f"Erro ao recuperar objeto {self.object_name} do bucket {self.bucket_name}: {e}")
            raise e

    def put_object(self, df):
        try:
            return s3_client.put_object(
                        Bucket=self.bucket_name,
                        Key=self.object_name,
                        Body= df
                    )  
        except Exception as e:
            self.logger.error(f"Erro ao salvar objeto {self.object_name} no bucket {self.bucket_name}: {e}")
            raise e     
