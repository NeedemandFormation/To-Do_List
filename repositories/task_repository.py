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
    query = "INSERT INTO task (title, description, is_done)" 
    "VALUES(%s, %s, %s)"
    values = (task_entity.title, task_entity.description, task_entity.is_done)

    cursor = self.connection.cursor()
    cursor.execute(query, values)
    self.connection.commit()

    return cursor.lastrowid
  
  def __del__(self):
    if hasattr(self, 'connection') and self.connection:
      if self.connection.is_connected():
        self.connection.close()
    else:
      print("No connection to close.")