from entities.task_entity import TaskEntity
from repositories.task_repository import TaskRepository

class TaskManager:
  def __init__(self, repository: TaskRepository):
    self.repository = repository

  def add_task(self, entity: TaskEntity):
    if(entity.title):
      entity.id = self.repository.create(entity)