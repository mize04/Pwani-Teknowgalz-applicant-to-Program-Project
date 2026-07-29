import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("pwani.db")

        # Enable foreign key constraints
        self.connection.execute("PRAGMA foreign_keys = ON")

        self.cursor = self.connection.cursor()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()