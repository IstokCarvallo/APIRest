from app.infrastructure.database import Database
from app.core.config import settings

class UserService:

    def __init__(self):
        self.db = Database(settings.DB_CONNECTION)

    def get_users(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, username FROM Users")

        users = []
        for row in cursor.fetchall():
            users.append({
                "id": row.id,
                "username": row.username
            })

        conn.close()
        return users