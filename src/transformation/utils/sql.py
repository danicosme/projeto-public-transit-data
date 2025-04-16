import duckdb

from utils.logger import LoggingService

class SqlService:
    def __init__(self):
        self.logger = LoggingService(name="SqlService").logger
    
    def format_query(self, sql_path, **kwargs):
        with open(sql_path, "r") as sql_file:
            query = sql_file.read().format(**kwargs)
        return query

    def execute_query(self, query):
        try:
            with duckdb.connect() as conn:
                df = conn.execute(query).fetchdf()
                return df
        except Exception as e:
            self.logger.error(f"Erro ao executar a query: {e}")
            raise e
    
    