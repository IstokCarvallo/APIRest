import pyodbc
from app.core.config import settings

def get_connection():
    try:
        connection_string = (
            f"DRIVER={{{settings.DB_DRIVER}}};"
            f"SERVER={settings.DB_SERVER};"
            f"DATABASE={settings.DB_DATABASE};"
            f"UID={settings.DB_USER};"
            f"PWD={settings.DB_PASSWORD};"
            f"Encrypt={settings.DB_ENCRYPT};"
            f"TrustServerCertificate={settings.DB_TRUST_CERT};"
        )

        conn = pyodbc.connect(connection_string, timeout=5)
        return conn

    except pyodbc.Error as ex:
        print(f"[ERROR DB] {ex}")
        raise