class Map:
    def __init__(self):
        pass
    def print_state(self):
        pass

class Room:
    def __init__(self):
        pass

class GreatHall(Room):
    pass

class HiddenRoom(Room):
    pass

class Bedroom(Room):
    pass

class Jail(Room):
    pass

class Galerie(Room):
    pass

class Kingroom(Room):
    pass

class TreasureRoom(Room):
    pass


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
        exit("You died... Try it again.")
