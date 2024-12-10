class TaskEntity:
  def __init__(self, id=None, title=None, description=None, created_at=None, updated_at=None):
    self.id = id
    self.title = title
    self.description = description
    self.is_done = False
    self.created_at = created_at
    self.updated_at = updated_at

  def __str__(self):
        return f"TaskEntity(id={self.id}, title={self.title}, description={self.description}, " \
               f"is_done={self.is_done}, created_at={self.created_at}, updated_at={self.updated_at})"
