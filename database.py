# routes/task_database.py
import sqlite3

class TaskDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('tasks.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                description TEXT,
                priority TEXT,
                is_urgent INTEGER,
                custom_metric TEXT,
                team_members TEXT
            )
        ''')
        self.conn.commit()

    def add_task(self, title, description, priority, is_urgent, custom_metric, team_members):
        self.cursor.execute('''
            INSERT INTO tasks (title, description, priority, is_urgent, custom_metric, team_members)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (title, description, priority, is_urgent, custom_metric, ','.join(team_members)))
        self.conn.commit()

    def get_tasks(self):
        self.cursor.execute('SELECT * FROM tasks')
        return self.cursor.fetchall()

    def delete_task(self, task_id):
        self.cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        self.conn.commit()
