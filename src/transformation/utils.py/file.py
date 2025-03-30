import requests
from zipfile import ZipFile

class FileManipulator:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def unzip_file(self):
        try:
            with ZipFile(self.file_path, 'r') as zip_ref:
                zip_ref.extractall(self.file_path.split(".zip")[0])
        except Exception as e:
            print(f"Erro ao extrair arquivo: {e}")
            return None