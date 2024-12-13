from managers.task_manager import TaskManager
from entities.task_entity import TaskEntity

class TaskController():
  def __init__(self, manager: TaskManager, view):
    self.manager = manager
    self.view = view

  def add_task(self):
    task_entity: TaskEntity = self.view.get_task()
    task_entity = self.manager.add_task(task_entity)

    if task_entity.id:
      self.view.display_added_task(task_entity)
      print("Success")
      self.view.display_task(task_entity)
    else:
      print("Task was not added to your list.")

  def get_tasks(self):
    tasks = self.manager.get_tasks()
    self.view.display_all_tasks(tasks)

  def delete_task(self, object):
    task_id = self.view.del_btns.id(object)

    is_deleted = self.manager.delete_task(task_id)

    if is_deleted:
      print(f"La tâche avec l'ID {task_id} a été supprimée avec succès.")
      self.get_tasks()
    else:
      print("Échec de la suppression : Tâche non trouvée.")

  def update_task(self, object):
    task_id = self.view.checkboxes.id(object)
    is_updated = self.manager.update_task(task_id)

    if is_updated:
      print(f"La tâche avec l'ID {task_id} a été modifée avec succès.")
      self.get_tasks()
    else:
      print("Échec de la modification : Tâche non trouvée.")
    return