# models/task.py
class Task:
    def __init__(self, task_id,title, description, priority, is_urgent, custom_metric, team_members=None):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.is_urgent = is_urgent
        self.custom_metric = custom_metric
        self.team_members = team_members if team_members is not None else []
