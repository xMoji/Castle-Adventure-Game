# to-do

#   -better state() output
#   - add more functions
def up(p,l,extra):
    x = p.pos_x-1
    y = p.pos_y
    move(p,l,x,y)

def down(p,l,extra):
    x = p.pos_x+1
    y = p.pos_y
    move(p,l,x,y)

def left(p,l,extra):
    x = p.pos_x
    y = p.pos_y-1
    move(p,l,x,y)

def right(p,l,extra):
    x = p.pos_x
    y = p.pos_y+1
    move(p,l,x,y)

def move(p,l,x,y):
## makes sure move position is in the index
    if x < 0 or y < 0:
        print("Whoops thats the border. Couldn't move player")
        return
    try:
        l[x][y].name
    except IndexError:
        print("Whoops thats the border. Couldn't move player")
        return
    if l[x][y].moveable:
        p.move(l,x,y)
    else:
        l[x][y].interract(p,l,x,y)

##rework
def print_map(player,level,extra):
    count = []
    for i in range(len(level)):
        for r in range(len(level[i])):
            try:
                if count[r] < len(level[i][r].name):
                    count[r] = len(level[i][r].name)
            except IndexError:
                count.append(len(level[i][r].name))

    print("Current Map: \n")
    for i in range(len(level)):
        for r in range(len(level[i])):
            print(level[i][r].name,end=(" "*(count[r]-len(level[i][r].name)+1)))
        print()



def help_commands(p,l,extra):
    for i in commands:
        print(i,end="  ")
    print()

def exit_game(*args):
    print("""You knifed yourself (last blood of you):
    File "main.py", line 12, in <death>
        kill@self
    File "/You/Died/succesfully", line 66, in rip
Suicide: Killed the Process""")
    exit(0)

def show_inv(p,l,extra):
    for i in p.inv:
        print(i,end= " ")
    print()



commands_help = """left/right/up/down: Moves the player left/right/up/down
                state: Prints the current map state
                help: Prints this help
                commands: Prints all availibe commands
                quit: leaves the game
                inventory: shows your inventory"""


def commands_help_start(*args):
    print(commands_help)


commands = {
        "left":left,
        "right":right,
        "up":up,
        "down":down,
        "state":print_map,
        "commands":help_commands,
        "help_commands": commands_help_start,
        "quit":exit_game,
        "inventory":show_inv,

}
