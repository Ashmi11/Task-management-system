import unittest
import timeit
from task import Task
from task_routes import TaskManager
from unittest.mock import patch
from tkinter import Tk
from task_manager_gui import TaskManagerGUI, TaskManager
from main import LoginWindow


class TestTaskManagementResponseTime(unittest.TestCase):
    def setUp(self):
        # Create a task manager
        self.task_manager = TaskManager()

    def test_add_task_response_time(self):
        # Measure the response time for adding a task
        add_time = timeit.timeit(
            lambda: self.task_manager.add_task("Sample Task", "Description", "Medium", False, "Metric", []),
            number=1000)

        print(f"Add Task Response Time: {add_time} seconds")

    def test_get_tasks_response_time(self):
        # Add a task to the manager for testing retrieval
        self.task_manager.add_task("Sample Task", "Description", "Medium", False, "Metric", [])

        # Measure the response time for getting tasks
        get_time = timeit.timeit(lambda: self.task_manager.get_tasks(), number=1000)

        print(f"Get Tasks Response Time: {get_time} seconds")

    def test_delete_task_response_time(self):
        # Add a task to the manager for testing deletion
        self.task_manager.add_task("Sample Task", "Description", "Medium", False, "Metric", [])

        # Measure the response time for deleting a task
        delete_time = timeit.timeit(lambda: self.task_manager.delete_task(1), number=1000)
        print(f"Delete Task Response Time: {delete_time} seconds")


class TestUserAuthentication(unittest.TestCase):

    @patch("builtins.input", side_effect=["admin", "admin"])
    def test_successful_authentication(self, mock_input):
        login_root = Tk()
        login_app = LoginWindow(login_root)

        with self.assertRaises(SystemExit):
            login_app.login()

    @patch("builtins.input", side_effect=["invalid_user", "invalid_password"])
    def test_failed_authentication(self, mock_input):
        login_root = Tk()
        login_app = LoginWindow(login_root)

        with self.assertRaises(SystemExit):
            login_app.login()


if __name__ == '__main__':
    unittest.main()
