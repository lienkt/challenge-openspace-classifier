
class Seat:
  """
  Represents a single seat in a table.

  A seat can either be free or occupied by a person (occupant).
  """
  def __init__(self, occupant: str = ""):
    """
    Initialize a Seat object.

    :param occupant: Name of the person occupying the seat.
                      If empty string, the seat is considered free.
    """
    self.free = True if occupant == "" else False
    self.occupant = occupant

  def set_occupant(self, name):
    """
    Assign a person to this seat and mark it as occupied.

    :param name: Name of the person to assign to the seat.
    """
    self.free = False
    self.occupant = name

  def remove_occupant(self):
    """
    Remove the person from the seat and mark it as free.
    """
    self.free = True
    self.occupant = ""

class Table:
  """
  Represents a table containing multiple seats.

  A table has a fixed capacity and manages seat assignments.
  """

  def __init__(self, capacity: int):
    """
    Initialize a Table with a given number of seats.

    :param capacity: Number of seats in the table.
    """
    self.capacity = capacity
    self.seats = [Seat() for _ in range(capacity)]

  def has_free_spot(self):
    """
    Check if the table has at least one free seat.

    :return: True if there is at least one free seat, otherwise False.
    """
    # Return bool value:
    for seat in self.seats:
      if seat.free == True:
        return True
    return False
  
  def find_free_spot(self):
    """
    Find the index of the first available seat.

    :return: Index of a free seat, or -1 if no free seat exists.
    """
    # Return free item index:
    for i in range(0, len(self.seats)):
      if self.seats[i].free == True:
        return i
    return -1

  def assign_seat(self, name):
    """
    Assign a person to the first available seat in the table.

    :param name: Name of the person to assign.
    """
    index = self.find_free_spot()
    if index != -1:
      self.seats[index].set_occupant(name)
    
  def left_capacity(self):
    """
    Count how many free seats are left in the table.

    :return: Number of available seats.
    """
    left_capacity = 0
    for seat in self.seats:
      if seat.free == True:
        left_capacity += 1
    return left_capacity
