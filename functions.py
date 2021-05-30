def leave(p,m):
    p.dies()

def print_commands(p, m):
    for i in Command_list:
        print(i, end=" ")
    for i in room_commands:
        print(i, end=" ")
    print("")

def enter(p,m):
    door_number = None
    if m.current_room == "Great Hall":
        print("Type in a door number from 1 to 4")
        try:
            door_number = int(input(">>> "))
        except ValueError:
            print("Please enter a number!")
        if door_number in range(1,5):
            m.enter(door_number-1, m)
        else:
            print("Numbers from 1 to 4....")
    else:
        print("To go back please type in back")

def go_back(p,m):
    if m.current_room == "Great Hall":
        print("You walked against a wall...")
    else:
        m.enter(5, m)

def print_help(p,m):
    print(help_text)


help_text = """
The goal of the game is to find the treasure room somewhere in the Castle. You can
equip yourself better by looting things. Also always be above ㊵ Health. But that
are enough hints. Now its gaming time yippe!!!

PS: Sometimes it seems to be a programm error when it says,
that the enterted,correct keyword isn't vaild. Just try the same keyword again and it'll work.
*b-r-u-h not fixable Programm Error*

Have fun and I hope you enjoy the game ♥ """


Command_list = {
    "help":print_help,
    "leave":leave,
    "commands":print_commands,
    "enter":enter,
    "back":go_back,
    }
