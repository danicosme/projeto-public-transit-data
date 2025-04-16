import os
from dotenv import load_dotenv

class Config:
    """Classe para gerenciar as configurações."""

    load_dotenv()

    BUCKET_NAME_PROCESSED = os.getenv("BUCKET_NAME_PROCESSED")