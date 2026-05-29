class Colleague:
  """
  Represents a colleague participating in the seating organization.

  Each colleague has:
  - a unique identifier
  - a name
  - a late status
  - a wishlist of preferred colleagues
  - a blacklist of colleagues to avoid
  """

  def __init__(
    self, 
    id: int, 
    name: str, 
    late: bool, 
    wishlist: list[int], 
    blacklist: list[int]):
    """
    Initialize a Colleague object.

    :param id: Unique identifier of the colleague.
    :param name: Name of the colleague.
    :param late: Indicates whether the colleague arrives late.
    :param wishlist: List of colleague IDs this person would like to sit with.
    :param blacklist: List of colleague IDs this person should not sit with.
    """
    self.id = id
    self.name = name
    self.late = late
    self.wishlist = wishlist
    self.blacklist = blacklist

  