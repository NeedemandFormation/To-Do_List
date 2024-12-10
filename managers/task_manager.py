from entities.task_entity import TaskEntity
from repositories.task_repository import TaskRepository
import time

class TaskManager:
  def __init__(self, repository: TaskRepository):
    self.repository = repository

  def add_task(self, entity: TaskEntity):
    if(entity.title):
      entity.created_at = time.time()
      entity.id = self.repository.create(entity)
    
    return entity