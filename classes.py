
class Map:
    def __init__(self):
        self.current_room = "Great Hall"
        self.map_state = [Bedroom("Bedroom"),Jail("Jail"),Galerie("Galerie"),Kingroom("Kingroom"),GreatHall("Great Hall"),TreasureRoom("Treasure Room")]
    def print_state(self):
        print("You are in the "+str(self.current_room))
    def enter(self, door_number, m):
        self.current_room = self.map_state[door_number].name
        self.map_state[door_number].enter(door_number, m)

class Room:
    def __init__(self, name):
        self.name = name
    def enter(self):
        pass

class GreatHall(Room):
    def __init__(self, name):
        Room.__init__(self,name)

class HiddenRoom(Room):
    def __init__(self, name):
            Room.__init__(self,name)

class Bedroom(Room):
    def __init__(self, name):
        Room.__init__(self,name)

class Jail(Room):
    def __init__(self, name):
        Room.__init__(self,name)
class Galerie(Room):
    def __init__(self, name):
        Room.__init__(self,name)
class Kingroom(Room):
    def __init__(self, name):
        Room.__init__(self,name)
class TreasureRoom(Room):
    def __init__(self, name):
        Room.__init__(self,name)


class Character:
    def __init__(self, ad, health, name):
        self.ad = ad
        self.health = health
        self.name = name
    def dies(self):
        print(self.name +"died.")

class Player(Character):
    def __init__(self, ad, health, name):
        Character.__init__(self, ad, health, name)
    def dies(self):
        quit("You died... Try it again.")
