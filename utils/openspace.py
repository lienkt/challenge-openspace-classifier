import random
import csv
import os

class Openspace:

  def __init__(self, tables: Table, number_of_tables: int):
    self.tables = tables
    self.number_of_tables = number_of_tables

  def organize(self, names):
    for name in names:
      table_index = self.random_free_table()
      seat_index = self.tables[table_index].find_free_spot()
      self.tables[table_index].seats[seat_index].set_occupant(name)
      
  def random_free_table(self):
      table_index = random.randint(0, self.number_of_tables - 1)
      current_table = self.tables[table_index]
      while current_table.has_free_spot() == False:
        table_index = random.randint(0, self.number_of_tables - 1)
        current_table = self.tables[table_index]
      return table_index

  def display(self):
    for i in range(0, len(self.tables)):
      print(f"\nPeople in table {i}:")
      for j in range(0, len(self.tables[i].seats)):
        print(f"Seat {j + 1}: {self.tables[i].seats[j].occupant}")
      print(f"Left capacity: {self.tables[i].left_capacity()}")

  def store(self, filename: str = "output.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # header
        writer.writerow(["Table", "Seat", "Name"])
        # content
        for table_index, table in enumerate(self.tables):
          for seat_index, seat in enumerate(table.seats):
              writer.writerow([
                table_index + 1,
                seat_index + 1,
                seat.occupant,
              ])
      