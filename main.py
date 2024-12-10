import sys
import os

from dotenv import load_dotenv
from repositories.task_repository import TaskRepository
from managers.task_manager import TaskManager
from views.task_view import TaskView
from controllers.task_controller import TaskController
from PyQt6.QtWidgets import QApplication

if (__name__ == "__main__"):
  load_dotenv()
  app = QApplication(sys.argv)
  repository = TaskRepository(host = os.getenv("DB_HOST"), database = os.getenv("DB_DATABASE"), user = os.getenv("DB_USER"), password = os.getenv("DB_PASSWORD"))
  manager = TaskManager(repository)
  view = TaskView()
  controller = TaskController(manager, view)

  view.connect_signals(controller)
  view.show()

  sys.exit(app.exec())