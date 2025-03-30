import os
from dotenv import load_dotenv

class Config:
    """Classe para gerenciar as configurações."""

    load_dotenv()

    REFRESH_TOKEN       = os.getenv("REFRESH_TOKEN")
    BUCKET_NAME         = os.getenv("BUCKET_NAME")
    API_TOKEN_URL       = os.getenv("API_TOKEN_URL")
    API_GET_DATA_URL    = os.getenv("API_GET_DATA_URL")