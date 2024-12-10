from entities.task_entity import TaskEntity

class TaskController():
  def __init__(self, manager, view):
    self.manager = manager
    self.view = view

  def add_task(self):
    task_entity: TaskEntity = self.view.get_task()
    task_entity = self.manager.add_task(task_entity)

    if task_entity.id:
      self.view.display_added_task(task_entity)
      print("Success")
    else:
      print("Task was not added to your list.")