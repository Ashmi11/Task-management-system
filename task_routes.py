# routes/task_routes.py
from database import TaskDatabase

class TaskManager:
    def __init__(self):
        self.db = TaskDatabase()

    def add_task(self, title, description, priority, is_urgent, custom_metric, team_members):
        self.db.add_task(title, description, priority, is_urgent, custom_metric, team_members)

    def get_tasks(self):
        tasks_from_db = self.db.get_tasks()
        return tasks_from_db  # No need to convert to Task objects

    def delete_task(self, task_id):
        self.db.delete_task(task_id)