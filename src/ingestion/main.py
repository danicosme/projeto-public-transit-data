import pytz

from datetime import datetime

from configuration.config import Config

from utils.api import ApiService
from utils.file import FileService
from utils.logger import LoggingService
from utils.s3 import S3Service

logger = LoggingService(name="main").logger

def lambda_handler(event, context):
    logger.info("Iniciando execução da Lambda")
    try:
        # Recupera o token da API
        logger.info("Recuperando Token da API")
        refresh_token = Config.REFRESH_TOKEN
        api_token = ApiService(url=Config.API_TOKEN_URL).get_api_token(refresh_token=refresh_token)

        # Recupera a URL do arquivo
        logger.info("Recuperando URL do arquivo")
        url_data = ApiService(url=Config.API_GET_DATA_URL).get_url_data(api_token=api_token)

        # Faz o download do arquivo
        logger.info("Fazendo download do arquivo")
        file = FileService(url=url_data).download_file()

        # Grava o arquivo no S3
        logger.info("Gravando arquivo no S3")
        bucket_name = Config.BUCKET_NAME
        current_datetime = datetime.now(pytz.timezone('America/Sao_Paulo'))
        ingestion_date = current_datetime.strftime("%Y-%m-%d")
        ingestion_hour = current_datetime.strftime("%H_%M_%S")
        object_name = f"{ingestion_date}/sp_trans_data_{ingestion_hour}.zip"
        S3Service(bucket_name=bucket_name, object_name=object_name).put_object(data=file)

        logger.info(f"Arquivo {object_name} gravado com sucesso no bucket {bucket_name}")
    except Exception as e:
        logger.error(f"Erro durante a execução da Lambda: {e}")
        raise


if __name__ == "__main__":
    lambda_handler(event={}, context={})
