import requests
from zipfile import ZipFile

from logger import LoggingService

class FileService:
    def __init__(self, url):
        self.logger = LoggingService(name="FileService").logger
        self.url = url

    def download_file(self):
        """Faz o download do arquivo zip."""
        try:
            response = requests.get(self.url)
            return response.content
        except Exception as e:
            self.logger.error(f"Erro no download do arquivo {self.url}: {e}")
            raise