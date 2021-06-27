from levels import level_1
from classes import *
from functions import *

player_name = None
while player_name == None:
    player_name = input("What is your name --> ")
    if len(player_name) >= 20:
        print("Thats a too long name")
        player_name = None

p = Player(player_name)
current_level = level_1

p.on_spawn(current_level)

while True:
    temp = input(">>> ").lower()
    if temp in commands:
        commands[temp](p,current_level,"##nothing")
    else:
        print("Please enter a vaild command")
