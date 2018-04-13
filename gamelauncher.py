from sys import exit
import os
cls = lambda: os.system('cls')

#make functiion return
def signinMenu():
    cls()
    while True:
        print("╔═══════╗")
        print("║ Setup ║")
        print("╠═══════╩══════════════════════════════════════╗")
        print("║please enter your initials for the scoreboard.║")
        print("╚══════════════════════════════════════════════╝")
        Initials = input("Initials:")
        if len(Initials) > 3 or len(Initials) < 1:
            print("ERROR: your intials may only be 3 characters in length!")
        else:
            global scoreboardIdentifier
            scoreboardIdentifier = Initials
            cls()
            verifyFileSym()
            break

    while True:
        print("╔═══════════════════════════╗")
        print("║ Instructions              ║")
        print("╠═══════════════╦═════════╦═╩══════════════╗")
        print("║               ║Controls:║                ║")
        print("║               ╚═════════╝                ║")
        print("║Move Left: A / Left Arrow Key             ║")
        print("║Move Right: D / Right Arrow Key           ║")
        print("║              ╔════════════╗              ║")
        print("║              ║How to play:║              ║")
        print("║              ╚════════════╝              ║")
        print("║Using the keys, move your ship so that it ║")
        print("║does not get hit by the falling asteroids.║")
        print("╚══════════════════════════════════════════╝")
        ReadyToPlay = input("Ready to play?(y, n):")
        if ReadyToPlay == "y" or ReadyToPlay == "yes":
            print(ReadyToPlay)
            print("Starting game!")
            break
        elif ReadyToPlay == "n" or ReadyToPlay == "no":
            print("quitting!")
            exit()
        elif ReadyToPlay == "devCon":
            print("debug would go here")
        else:
            cls()
            print("ERROR: That is not a valid answer!")

def getScore(score):
    print(score)
    print(scoreboardIdentifier)
def verifyFileSym():
    localContent = ""
    scoreboard_local = open("scoreboardLocals","r")
    localContent = scoreboard_local.readlines()
    print(localContent)
