from PyQt6.QtWidgets import (
  QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox,
  QButtonGroup
  )
from entities.task_entity import TaskEntity
from controllers.task_controller import TaskController
from datetime import datetime

#https://www.pythonguis.com/tutorials/python-classes/#using-classes-in-pyqt-gui-apps
class TaskView(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Gestion des tâches")
    self.setGeometry(100, 100, 600, 400)

    self.main_layout: QVBoxLayout = QVBoxLayout()

    self.form_layout = QVBoxLayout()
    self.title_input = self.add_form_input("Titre")
    self.description_input = self.add_form_input("Description")

    self.buttons_layout = QHBoxLayout()
    self.add_button = QPushButton("Ajout")
    self.buttons_layout.addWidget(self.add_button)

    self.tasks_layout = QVBoxLayout()
    self.del_btns = QButtonGroup()
    self.checkboxes = QButtonGroup()
    self.checkboxes.setExclusive(False)

    self.main_layout.addLayout(self.form_layout)
    self.main_layout.addLayout(self.buttons_layout)
    self.main_layout.addLayout(self.tasks_layout)
    self.setLayout(self.main_layout)

  def add_form_input(self, text):
    layout = QHBoxLayout()
    label = QLabel(text)
    field = QLineEdit()

    layout.addWidget(label)
    layout.addWidget(field)
    self.form_layout.addLayout(layout)

    return field
  
  def get_task(self):
    return TaskEntity(
      title = self.title_input.text(),
      description = self.description_input.text()
    )
  
  def display_added_task(self, task: TaskEntity):
    self.title_input.setText("")
    self.description_input.setText(task.description)

  def display_task(self, task: TaskEntity):
    layout = QHBoxLayout()
    converted_date = datetime.fromtimestamp(task.created_at).strftime("%d/%m/%Y %H:%M") if not task.updated_at else datetime.fromtimestamp(task.updated_at).strftime("%d/%m/%Y %H:%M")
    checkbox = QCheckBox(f"{converted_date} : {task.title}", self)
    checkbox.setChecked(task.is_done)
    button = QPushButton("Supprimer")
    description = QLabel(task.description)

    self.del_btns.addButton(button, task.id)
    self.checkboxes.addButton(checkbox, task.id)

    layout.addWidget(checkbox)
    layout.addWidget(button)
    layout.addWidget(description)
    self.tasks_layout.addLayout(layout)
    self.tasks_layout.addWidget(description)

  def reset_layout(self, layout):
    if layout is not None:
      while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()
        if widget is not None:
          widget.deleteLater()
        else:
          self.reset_layout(item.layout())

  def display_all_tasks(self, tasks: list[TaskEntity]):
    self.reset_layout(self.tasks_layout)
    for task in tasks:
      self.display_task(task)
  
  def connect_signals(self, controller: TaskController):
    self.add_button.clicked.connect(controller.add_task)
    controller.get_tasks()
    self.del_btns.buttonClicked.connect(controller.delete_task)
    self.checkboxes.buttonClicked.connect(controller.update_task)