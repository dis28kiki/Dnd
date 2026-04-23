import psycopg2


class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="dnd",
            user="master",
            password="qwe123",
            host="localhost",
            port="5432",
        )
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()

    def execute(self, query, params=None):
        self.cursor.execute(query, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()


db = Database()
