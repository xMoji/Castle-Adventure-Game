from random import randint
from tables import loot_table_chest

class Field:
    def interract(self,p,l,x,y):
        print("Interracted with "+self.name)
    @staticmethod
    def change_field(level,x,y,class_name):
        level[x][y] = class_name()

class Player():
    def __init__(self,name):
        self.name = name
        self.description = "Thats you"
        self.pos_x = 0
        self.pos_y = 1
        self.moveable = False
        self.inv = []
    def on_spawn(self,l):
        l[self.pos_x][self.pos_y] = self
    def move(self,l,x,y):
        ##everything needed got checked before
        Field.change_field(l,self.pos_x,self.pos_y,Empty)
        l[x][y] = self
        ##Control
        ##print("Move from " + str(self.pos_x)+","+str(self.pos_y) +"to "+ str(x)+","+str(y))
        self.pos_x = x
        self.pos_y = y
        print("Moved Player")




class Bed(Field):
    def __init__(self):
        self.description = "You sleep here"
        self.name = "Bed"
        self.moveable = False

class Empty(Field):
    def __init__(self):
        self.description = "On this field is nothing"
        self.name = "Emtpy"
        self.moveable = True


class Chest(Field):
    def __init__(self):
        self.description = "You can loot the chest on this Field"
        self.name = "Chest"
        self.moveable = False
    def interract(self,player,level,x,y):
        print("You are looting a chest yay")
        rand_num = randint(1,2)
        print(loot_table_chest[rand_num]+" was found by "+player.name)
        player.inv.append(loot_table_chest[rand_num])
        Field.change_field(level,x,y,Empty)

class Door(Field):
    def __init__(self, locked = False):
        self.description = "Open that door"
        self.name = "Door"
        self.locked = locked
        self.moveable = False
    def interract(self,player,level,x,y):
        if self.locked:
            pass
            ## add a key class + a check if the player has the key needed
        else:
            print("Opened door")
            Field.change_field(level,x,y,Empty)


class Wall(Field):
    def __init__(self):
        self.description = "Wall"
        self.name = "Wall"
        self.moveable = False
    def interract(self,player,level,x,y):
        print("Thats a wall and no door...")
        return
