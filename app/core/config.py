class Settings:
    DB_CONNECTION = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=MiDB;"
        "UID=sa;"
        "PWD=TuPassword;"
        "TrustServerCertificate=yes;"
    )

settings = Settings()