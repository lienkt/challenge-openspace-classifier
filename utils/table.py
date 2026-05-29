
class Seat:

  def __init__(self, occupant: str = ""):
    self.free = True if occupant == "" else False
    self.occupant = occupant

  def set_occupant(self, name):
    self.free = False
    self.occupant = name

  def remove_occupant(self):
    self.free = True
    self.occupant = ""

class Table:

  def __init__(self, capacity: int):
    self.capacity = capacity
    self.seats = [Seat() for _ in range(capacity)]

  def has_free_spot(self):
    # Return bool value:
    for seat in self.seats:
      if seat.free == True:
        return True
    return False
  
  def find_free_spot(self):
    # Return free item index:
    for i in range(0, len(self.seats)):
      if self.seats[i].free == True:
        return i
    return -1

  def assign_seat(self, name):
    self.seats.append(name)
    
  def left_capacity(self):
    left_capacity = 0
    for seat in self.seats:
      if seat.free == True:
        left_capacity += 1
    return left_capacity
