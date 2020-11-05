# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
  def __init__(self, name, description, location):
    self.name = name
    self.description = description
    self.location = location
    print(self)
    
  def __str__(self):
    return f"{self.name} is {self.description}. Current location: {self.location}."