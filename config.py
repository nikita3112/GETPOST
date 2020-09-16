import sqlite3


class SQLite:
    def __init__(self, databse_file):
        self.connection = sqlite3.connect(databse_file)
        self.cursor = self.connection.cursor()
    
    def find(self, artist):
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM album WHERE artist = '{artist}'").fetchall()
    
    def get_ids(self):
        with self.connection:
            return self.cursor.execute(f"SELECT id FROM album").fetchall()
    
    def add(self, a):
        with self.connection:
            return self.cursor.execute(f"INSERT INTO album VALUES ('{a['id']}', '{a['year']}', '{a['artist']}', '{a['genre']}', '{a['album']}')")

    def check_name(self, name):
        with self.connection:
            result = self.cursor.execute(f"SELECT * FROM album WHERE album = '{name}'").fetchall()
            return bool(result)