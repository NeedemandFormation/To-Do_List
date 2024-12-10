from PyQt6.QtWidgets import (
  QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
  )
from entities.task_entity import TaskEntity
from controllers.task_controller import TaskController

#https://www.pythonguis.com/tutorials/python-classes/#using-classes-in-pyqt-gui-apps
class TaskView(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Gestion des tâches")
    self.setGeometry(100, 100, 600, 400)

    self.layout: QVBoxLayout = QVBoxLayout()

    self.form_layout = QVBoxLayout()
    self.title_input = self.add_form_input("Titre")
    self.description_input = self.add_form_input("Description")

    self.buttons_layout = QHBoxLayout()
    self.add_button = QPushButton("Ajout")
    self.buttons_layout.addWidget(self.add_button)

    # layouts = [self.form_layout, self.buttons_layout]

    # for layout in layouts:
    #   self.layout.addLayout(layout)

    self.layout.addLayout(self.form_layout)
    self.layout.addLayout(self.buttons_layout)
    self.setLayout(self.layout)

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
  
  def connect_signals(self, controller: TaskController):
    self.add_button.clicked.connect(controller.add_task)