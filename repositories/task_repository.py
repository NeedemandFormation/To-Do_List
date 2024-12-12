import mysql.connector

from mysql.connector import Error
from entities.task_entity import TaskEntity

class TaskRepository:
  def __init__(self, host, database, user, password):
    self.connection = None

    try:
      self.connection = mysql.connector.connect(
        host = host,
        port = 3306,
        database = database,
        user = user,
        password = password
      )
      if (self.connection.is_connected()):
        print("You are now connected to the database")
      else:
        print("Failed connection")
    except mysql.connector.Error as err:
      print(f"Database connection error: {err}.")
      self.connection = None

  def create(self, task_entity: TaskEntity) ->int:
    query = """
    INSERT INTO task (title, description, is_done, created_at)
    VALUES(%s, %s, %s, %s)
    """
    values = (task_entity.title, task_entity.description, task_entity.is_done, task_entity.created_at)

    try:
      cursor = self.connection.cursor()
      cursor.execute(query, values)
      self.connection.commit()

      return cursor.lastrowid
    except Error as err:
      print(f"Couldn't add task: {err}")
      return None
    
  def read(self):
    query = "SELECT * FROM task"

    try:
      cursor = self.connection.cursor(dictionary=True)
      cursor.execute(query)
      tasks = cursor.fetchall()

      return [TaskEntity(
        task["id"],
        task["title"],
        task["created_at"],
        task["description"],
        task["updated_at"],
        task["is_done"]
        ) for task in tasks]
    
    except Error as e:
      print(f"Erreur lors de la récupération des livres : {e}")

      return []

  def delete(self, id):
    query = "DELETE FROM task WHERE id = %s"

    try:
      cursor = self.connection.cursor()
      cursor.execute(query, (id,))
      self.connection.commit()
      return cursor.rowcount > 0
    except Error as err:
      print(f"Erreur lors de la suppression de la tâche : {err}")
      return False 

  def __del__(self):
    if hasattr(self, 'connection') and self.connection:
      if self.connection.is_connected():
        self.connection.close()
    else:
      print("No connection to close.")