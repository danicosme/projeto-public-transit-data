import duckdb

from utils.logger import LoggingService

class SqlService:
    def __init__(self, query: str = None):
        self.logger = LoggingService(name="DuckDbService").logger
        self.connection_string = duckdb.connect()
        self.query = query
    
    def format_query(self, sql_path, **kwargs):
        with open(sql_path, "r") as sql_file:
            query = sql_file.read().format(**kwargs)
        return query

    def execute_query(self, query):
        return self.connection_string.execute(query).fetchdf()
    
    