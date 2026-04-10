import pyodbc

class Database:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def get_connection(self):
        try:
            conn = pyodbc.connect(self.connection_string)
            return conn
        except Exception as e:
            print(f"Error conexión DB: {e}")
            raise