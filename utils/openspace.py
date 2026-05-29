import random
from utils.file_utils import store_file
from utils.table import Table
from utils.colleague import Colleague

class Openspace:
  """
  Represents an office space containing multiple tables.

  This class is responsible for:
  - Organizing colleagues into tables
  - Randomly assigning seats
  - Displaying the seating arrangement
  - Exporting the final layout to a file
  """

  def __init__(self, tables: list[Table], number_of_tables: int):
    """
    Initialize the Openspace with a list of tables.

    :param tables: List of Table objects representing the workspace.
    :param number_of_tables: Total number of tables in the space.
    """
    self.tables = tables
    self.number_of_tables = number_of_tables

  def organize(self, colleagues: list[Colleague]):
    """
    Assign each colleague to a random table with a free seat.

    :param colleagues: List of Colleague objects to be placed in the space.
    """
    for colleague in colleagues:
      table_index = self.random_free_table()
      self.tables[table_index].assign_seat(colleague.name)
  
  def random_free_table(self):
      """
      Safely pick a random table that has free seats.

      :return: Index of a table with available seats.
      :raises Exception: if no tables have free seats.
      """
      available_tables = [
        i for i, table in enumerate(self.tables)
        if table.has_free_spot()
      ]
      if not available_tables:
        raise Exception("No free seats available in any table.")

      return random.choice(available_tables)

  def display(self):
    """
    Print the current seating arrangement in a readable format.
    """
    for i, table in enumerate(self.tables):
      print(f"\nPeople in table {i + 1}:")
      for j, seat in enumerate(table.seats):
        print(f"Seat {j + 1}: {seat.occupant}")
      print(f"Left capacity: {table.left_capacity()}")

  def store(self, filepath: str = "output.csv"):
    """
    Export the seating arrangement to a file.

    :param filepath: Path of the output file (default: output.csv)
    """
    store_file(self.tables, filepath)