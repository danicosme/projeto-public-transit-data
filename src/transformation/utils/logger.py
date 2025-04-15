import logging
from typing import Optional

class LoggingService:
    def __init__(self, name: str = __name__, level: int = logging.INFO, formatter: Optional[str] = None):
        """Inicializa o serviço de logging."""
        self.logger = logging.getLogger(name)

        # Evita adicionar múltiplos handlers ao mesmo logger
        if not self.logger.hasHandlers():
            self.logger.setLevel(level)

            ch = logging.StreamHandler()
            ch.setLevel(level)

            log_format = formatter or '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            ch.setFormatter(logging.Formatter(log_format))

            self.logger.addHandler(ch)