from utils.table import Table
from utils.openspace import Openspace
import csv
import os
import json

def main():
  # Check current working directory: os.getcwd()
  base_dir = os.path.dirname(__file__)
  config_filepath = os.path.join(base_dir, "config.json")
  input_filepath = os.path.join(base_dir, "new_colleagues.csv")
  output_filepath = os.path.join(base_dir, "output.csv")

  with open(config_filepath, "r", encoding="utf-8") as f:
      config = json.load(f)
  NUMBER_OF_TABLES = config["NUMBER_OF_TABLES"]
  TABLE_CAPACITY = config["TABLE_CAPACITY"]
  

  # Creates a list that contains all the colleagues names
  new_collegues = []
  with open(input_filepath, "r", encoding="utf-8") as f:
      reader = csv.reader(f)
      for row in reader:
          new_collegues.append(row[0])

  number_of_people = len(new_collegues)
  amount_table_in_demand = number_of_people // TABLE_CAPACITY
  if amount_table_in_demand > NUMBER_OF_TABLES:
    if number_of_people % TABLE_CAPACITY == 0:
      NUMBER_OF_TABLES = amount_table_in_demand
    else:
      NUMBER_OF_TABLES = amount_table_in_demand + 1
    print(f"The table in demand is {NUMBER_OF_TABLES}")
       

  tables = [Table(TABLE_CAPACITY) for _ in range(NUMBER_OF_TABLES)]

  # create an OpenSpace()
  open_space = Openspace(tables, NUMBER_OF_TABLES)

  # assign a colleague randomly to a table
  open_space.organize(new_collegues)
  open_space.display()

  # save the seat assigments to a new file
  open_space.store(output_filepath)

  # display assignments in the terminal
  open_space.display()

  #
  while True:
    print("\n=== ROOM MENU ===")
    print("1. How much seats are in the room")
    print("2. How much people are in the room")
    print("3. How much seats are left")
    print("4. Exit")

    choise = input("Choose an option: ")

    match choise:
      case "1":
        print(f"Total seats in the room: {NUMBER_OF_TABLES*TABLE_CAPACITY}")

      case "2":
        print(f"Total people in the room: {number_of_people}")

      case "3":
        print(f"Total seats left: {(NUMBER_OF_TABLES*TABLE_CAPACITY) - number_of_people}")
    
      case "4":
        print("Goodbye!")
        break
           

if __name__ == "__main__":
    main()










