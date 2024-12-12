class TaskEntity:
  def __init__(self, id = None, title = None, created_at = 0, description = None, updated_at = None, is_done = False):
    self.id = id
    self.title = title
    self.created_at = created_at
    self.description = description
    self.updated_at = updated_at
    self.is_done = is_done

  def __str__(self):
        return f"TaskEntity(id={self.id}, title={self.title}, description={self.description}, " \
               f"is_done={self.is_done}, created_at={self.created_at}, updated_at={self.updated_at})"
