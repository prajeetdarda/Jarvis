from plugin import plugin
import os

@plugin("infob17134")
def infoB17134(jarvis, s):
    jarvis.say("Welcome to the info plugin of Prajeet roll num B17134. Please select one of the options below:\n[F]ull name // prints your full name\n[H]ometown // prints your hometown\nFavourite [M]ovie // prints your fav movie\nFavourite [S]portsperson // prints your fav sportsperson\nLaunch [P]ython program written by me // launch a (short)// python program")
    inp = input()
    if inp == "F":
        jarvis.say("Prajeet Darda")
        pass
    if inp == "H":
        jarvis.say("Udaipur")
        pass
    if inp == "M":
        jarvis.say("Inception")
        pass
    if inp == "S":
        jarvis.say("Messi")
        pass
    if inp == "P":
        os.system("python /local/user/Jarvis/jarviscli/plugins/my.py")
        pass

