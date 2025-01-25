import sqlite3

class Database:
    def __init__(self, db_name="bot_database.db"):
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                message TEXT NOT NULL
            )
        """)
        self.connection.commit()

    def save_message(self, username, message):
        self.cursor.execute("INSERT INTO messages (username, message) VALUES (?, ?)", (username, message))
        self.connection.commit()

    def get_user_messages(self, username):
        self.cursor.execute("SELECT message FROM messages WHERE username = ?", (username,))
        return [row[0] for row in self.cursor.fetchall()]

    def close(self):
        self.connection.close()
