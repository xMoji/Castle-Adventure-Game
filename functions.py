def leave(p,m):
    p.dies()

def print_commands(p, m):
    for i in Command_list:
        print(i, end=" ")
    print("")

def print_help(p,m):
    print(help_text)


help_text = """
The goal of the game is to find the treasure room somewhere in the Castle. You can
equip yourself better by looting things. Also always be above ㊵ Health. But that
are enough hints. Now its gaming time yippe!!!

PS: Sometimes it seems to be a programm error when it says,
that the enterted,correct keyword isn't vaild. Just try the same keyword again and it'll work.
*bruh not fixable Programm Error*

Have fun and I hope you enjoy the game ♥ """


Command_list = {
    "help":print_help,
    "leave":leave,
    "commands":print_commands,
    }
