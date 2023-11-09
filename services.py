import sqlite3

con = sqlite3.connect("database.db")
con.row_factory = sqlite3.Row
cursor = con.cursor()


class TaskService:
    def create(self, title: str, status: str):
        cursor.execute("INSERT INTO tasks (title, status) VALUES (?, ?)",
                       (title, status))
        con.commit()

    def findByTitle(self, title: str):
        cursor.execute("SELECT * FROM tasks WHERE title = ?", (title,))
        return cursor.fetchone()

    def findAll(self):
        cursor.execute("SELECT * FROM tasks")
        return cursor.fetchall()

    def deleteByTitle(self, title: str):
        cursor.execute("DELETE FROM tasks WHERE title = ?", (title,))
        con.commit()

    def updateByTitle(self, title: str, status: str):
        cursor.execute(f"UPDATE tasks SET status = '{status}' WHERE title = '{title}'")
        con.commit()
