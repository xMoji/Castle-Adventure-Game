from functions import *
from classes import *





if __name__ == "__main__":
    print("Type help to get the help test. Type commands to get the command list")
    map = Map()
    p = Player(100, 400, input("Enter your name: "))
    while True:
        command = input("> ").lower().split(" ")
        if command[0] in Command_list:
            Command_list[command[0]](p,map)
        elif command[0] in room_commands:
            room_commands[command[0]](p,map)
        else:
            print("Enter vaild command")
