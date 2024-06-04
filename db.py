import time
import psycopg2
from paper import Paper

class Database:
    def __init__(self, database_url) -> None:
        self.con = psycopg2.connect(database_url)
        self.cur = self.con.cursor()

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.close()

    def create_table(self):
        q = """
        CREATE TABLE IF NOT EXISTS papers (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        self.cur.execute(q)
        self.con.commit()

    def insert_paper(self, paper: Paper):
        q = """
        INSERT INTO papers (id, title)
        VALUES (%s, %s)
        ON CONFLICT (id) DO NOTHING;
        """
        self.cur.execute(q, (paper.id, paper.title))
        self.con.commit()

    def query_table(self, search_query=None, sort_column=None, sort_order=None):
        query = "SELECT id, title, created_at FROM papers "

        if search_query:
            query += " WHERE "
            query += "title LIKE %s"
            query += f" ORDER BY {sort_column} " if sort_column is not None else ""
            query += "DESC" if sort_order != "from low to high" else "ASC"
            print(query, search_query)
            self.cur.execute(query + ' ', ('%' + search_query + '%', ))
        elif sort_column:
            query += f" ORDER BY {sort_column} "
            query += "DESC" if sort_order != "from low to high" else "ASC"
            self.cur.execute(query + ' ')
        else:
            self.cur.execute(query + ' ')

        return self.cur.fetchall()