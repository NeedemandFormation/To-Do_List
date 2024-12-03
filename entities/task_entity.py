class TaskEntity:
  def __init__(self, id, title, description, created_at, updated_at=None):
    self.id = id
    self.title = title
    self.description = description
    self.is_done = False
    self.created_at = created_at
    self.updated_at = updated_at
