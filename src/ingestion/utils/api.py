import requests
import json

from utils.logger import LoggingService

class ApiService:
    def __init__(self, url):
        self.logger = LoggingService(name="ApiService").logger
        self.url = url

    def get_api_token(self, refresh_token):
        """Obtém o token de acesso da API."""
        headers = {
            'Content-Type': 'application/json'
        }

        data = {
            "refresh_token": refresh_token
        }

        try:
            response = requests.post(self.url, headers=headers, data=json.dumps(data))
            return response.json()['access_token']
        except Exception as e:
            self.logger.error(f"Erro ao solicitar token: {e}")
            raise


    def get_url_data(self, api_token):
        """Obtém a URL do dataset mais recente."""
        headers = {
            "Authorization": f"Bearer {api_token}",
            "Accept": "application/json" 
        }

        try:
            response = requests.get(self.url, headers=headers)
            return response.json()["latest_dataset"]["hosted_url"]
        except Exception as e:
            self.logger.error(f"Erro na requisição: {e}")
            raise
