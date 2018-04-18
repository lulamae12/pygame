from sys import exit
import os
cls = lambda: os.system('cls')
score = 0
scoreboardIdentifier = ''
PURPLE = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
#make functiion return
def signinMenu():
    print(ENDC + "")
    cls()
    while True:
        print(GREEN + "╔═══════╗")
        print("║ Setup ║")
        print("╠═══════╩══════════════════════════════════════╗")
        print("║please enter your initials for the scoreboard.║")
        print("╚══════════════════════════════════════════════╝")
        Initials = input("Initials:" + ENDC)
        if Initials == "devCon":
            break
            debugConsole()

        elif len(Initials) != 3:
            cls()
            print(RED + "ERROR: your intials should be 3 characters in length!" + ENDC)

        elif " " in Initials:
            cls()
            print(RED + "ERROR: your intials may not contain spaces!" + ENDC)

        else:
            global scoreboardIdentifier
            scoreboardIdentifier = Initials
            scoreboardIdentifier = scoreboardIdentifier.upper()
            cls()
            verifyFileSym()
            break

    while True:
        print(GREEN + "╔═══════════════════════════╗")
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
        ReadyToPlay = input("Ready to play?(y, n):" + ENDC)
        if ReadyToPlay == "y" or ReadyToPlay == "yes" or ReadyToPlay == "Y":
            print(ReadyToPlay)
            print("Starting game!")
            break
        elif ReadyToPlay == "n" or ReadyToPlay == "no" or ReadyToPlay == "N":
            print("quitting!")
            exit()
        else:
            cls()
            print(RED + "ERROR: That is not a valid answer!"+ ENDC)
def debugConsole():
    print("you have entered the debug console:")

def getScore(score):
    score = score
    updateScoreboard(score)
def verifyFileSym():
    localContent = ""
    hardcodedContent = ""
    try:
        scoreboard_local = open("scoreboardLocals.txt","r")#open local cached scoreboard
        localContent = scoreboard_local.readlines()#read lines
        scoreboard_hardcode = open("C:/Users/Public/Documents/SH.txt","r")#open "backup file"
        hardcodedContent = scoreboard_hardcode.readlines()#readlines
        if localContent != hardcodedContent:
                scoreboard_hardcode = open("C:/Users/Public/Documents/SH.txt","w")
                SHLinesOfText = ["NAME","\n","TLS","\n","SCORE","\n","000.00"]
                scoreboard_hardcode.writelines(SHLinesOfText)
                scoreboard_hardcode.close()
                localContent = open("scoreboardLocals.txt","w")
                localContentTEXT = ["NAME","\n","TLS","\n","SCORE","\n","000.00"]
                localContent.writelines(localContentTEXT)
                localContent.close()
    except:#if file dosent exist make new default one
        print("file not found")
        scoreboard_hardcode = open("C:/Users/Public/Documents/SH.txt","w")
        SHLinesOfText = ["NAME","\n","TLS","\n","SCORE","\n","000.00"]
        scoreboard_hardcode.writelines(SHLinesOfText)
        scoreboard_hardcode.close()
        localContent = open("scoreboardLocals.txt","w")
        localContentTEXT = ["NAME","\n","TLS","\n","SCORE","\n","000.00"]
        localContent.writelines(localContentTEXT)
        localContent.close()


    print(hardcodedContent)
    print(localContent)
def updateScoreboard(score):
    currentScoreL = open("scoreboardLocals.txt","r+")
    localLines = currentScoreL.readlines()
    nameLocal = localLines[1]
    scoreLocal = float(localLines[3])

    currentScoreH = open("C:/Users/Public/Documents/SH.txt","r+")
    hardcodeLines = currentScoreH.readlines()
    nameHardcode = hardcodeLines[1]
    scoreHardcode = (hardcodeLines[3])




    if float(score) >= scoreLocal:
        scoreboard_local = open("scoreboardLocals.txt","w")
        scoreboard_hardcode = open("C:/Users/Public/Documents/SH.txt","w")

        scoreLocal = score
        scoreHardcode = score
        nameLocal = scoreboardIdentifier
        nameHardcode = scoreboardIdentifier

        localContentTEXT = ["NAME","\n",nameLocal,"\n","SCORE","\n",scoreLocal]
        SHLinesOfText = ["NAME","\n",nameHardcode,"\n","SCORE","\n",scoreHardcode]
        scoreboard_local.writelines(localContentTEXT)
        scoreboard_hardcode.writelines(SHLinesOfText)
        scoreboard_local.close()
        scoreboard_hardcode.close()
        cls()
        print("╔════════════════╗")
        print("║ New Highscore! ║")
        print("╠════════════════╩════════════════════╗")
        print("║ Current Highscore: ",str(scoreboardIdentifier),str(score),"Feet  ║")
        print("╚═════════════════════════════════════╝")
    else:
        scoreboard_local = open("scoreboardLocals.txt","r")
        lines = scoreboard_local.readlines()
        HighscoreName = lines[1]
        HighscoreScore = lines[3]

        scoreboard_local.close()
        cls()
        print(GREEN + "╔═════════════════════════════════════╗")
        print("║ Current Highscore: " + ENDC + YELLOW + str(HighscoreName.strip()),str(HighscoreScore.strip()),"Feet" + ENDC + GREEN + "   ║") #strip gets rid of newline
        print("║                                     ║")
        print("║ Your score: " + ENDC + PURPLE + scoreboardIdentifier,str(score),"Feet" + ENDC + GREEN + "          ║")
        print("╚═════════════════════════════════════╝")
    currentScoreL.close()
    currentScoreH.close()
