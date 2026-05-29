import random
from utils.file_utils import store_file
from utils.table import Table
from utils.colleague import Colleague

class Openspace:

  def __init__(self, tables: list[Table], number_of_tables: int):
    self.tables = tables
    self.number_of_tables = number_of_tables

  def organize(self, colleagues: list[Colleague]):
    for colleague in colleagues:
      table_index = self.random_free_table()
      seat_index = self.tables[table_index].find_free_spot()
      self.tables[table_index].seats[seat_index].set_occupant(colleague.name)
      
  def organize2(self, names):
    for name in names:
      table_index = self.random_free_table()
      seat_index = self.tables[table_index].find_free_spot()
      s
  
  def random_free_table(self):
      table_index = random.randint(0, self.number_of_tables - 1)
      current_table = self.tables[table_index]
      while current_table.has_free_spot() == False:
        table_index = random.randint(0, self.number_of_tables - 1)
        current_table = self.tables[table_index]
      return table_index

  def display(self):
    for i in range(0, len(self.tables)):
      print(f"\nPeople in table {i + 1}:")
      for j in range(0, len(self.tables[i].seats)):
        print(f"Seat {j + 1}: {self.tables[i].seats[j].occupant}")
      print(f"Left capacity: {self.tables[i].left_capacity()}")

  def store(self, filepath: str = "output.csv"):
    store_file(self.tables, filepath)