from sys import exit
import os
cls = lambda: os.system('cls')
score = 0
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
    score = score
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
                SHLinesOfText = ["PLACE","\n","1ST","\n","Name1Name","\n","TLS","\n","Name1Score","\n","000","\n","\n","\n",
                "PLACE","\n","2ND","\n","Name2Name","\n","TLS","\n","Name2Score","\n","000","\n","\n","\n","PLACE","\n","3RD","\n","Name3Name","\n","TLS","\n","Name3Score","\n","000",
                "\n","\n","\n","PLACE","\n","4TH","\n","Name4Name","\n","TLS","\n","Name4Score","\n","000","\n","\n","\n","PLACE","\n","5TH","\n","Name5Name","\n","TLS",
                "\n","Name5Score","\n","000","\n","\n","\n",]
                scoreboard_hardcode.writelines(SHLinesOfText)
                scoreboard_hardcode.close()
                localContent = open("scoreboardLocals.txt","w")
                localContentTEXT = ["PLACE","\n","1ST","\n","Name1Name","\n","TLS","\n","Name1Score","\n","000","\n","\n","\n",
                "PLACE","\n","2ND","\n","Name2Name","\n","TLS","\n","Name2Score","\n","000","\n","\n","\n","PLACE","\n","3RD","\n","Name3Name","\n","TLS","\n","Name3Score","\n","000",
                "\n","\n","\n","PLACE","\n","4TH","\n","Name4Name","\n","TLS","\n","Name4Score","\n","000","\n","\n","\n","PLACE","\n","5TH","\n","Name5Name","\n","TLS",
                "\n","Name5Score","\n","000","\n","\n","\n",]
                localContent.writelines(localContentTEXT)
                localContent.close()
    except:#if file dosent exist make new default one
        print("file not found")
        scoreboard_hardcode = open("C:/Users/Public/Documents/SH.txt","w")
        SHLinesOfText = ["PLACE","\n","1ST","\n","Name1Name","\n","TLS","\n","Name1Score","\n","000","\n","\n","\n",
        "PLACE","\n","2ND","\n","Name2Name","\n","TLS","\n","Name2Score","\n","000","\n","\n","\n","PLACE","\n","3RD","\n","Name3Name","\n","TLS","\n","Name3Score","\n","000",
        "\n","\n","\n","PLACE","\n","4TH","\n","Name4Name","\n","TLS","\n","Name4Score","\n","000","\n","\n","\n","PLACE","\n","5TH","\n","Name5Name","\n","TLS",
        "\n","Name5Score","\n","000","\n","\n","\n",]
        scoreboard_hardcode.writelines(SHLinesOfText)
        scoreboard_hardcode.close()
        localContent = open("scoreboardLocals.txt","w")
        localContentTEXT = ["PLACE","\n","1ST","\n","Name1Name","\n","TLS","\n","Name1Score","\n","000","\n","\n","\n",
        "PLACE","\n","2ND","\n","Name2Name","\n","TLS","\n","Name2Score","\n","000","\n","\n","\n","PLACE","\n","3RD","\n","Name3Name","\n","TLS","\n","Name3Score","\n","000",
        "\n","\n","\n","PLACE","\n","4TH","\n","Name4Name","\n","TLS","\n","Name4Score","\n","000","\n","\n","\n","PLACE","\n","5TH","\n","Name5Name","\n","TLS",
        "\n","Name5Score","\n","000","\n","\n","\n",]
        localContent.writelines(localContentTEXT)
        localContent.close()


    print(hardcodedContent)
    print(localContent)
def updateScoreboard():
    scoreboardLines = open("scoreboardLocals.txt", "r+")
    lines = scoreboardLines.readlines()
    firstPlaceIntitial = lines[4]
    firstPlaceScore = float(lines[6])

    secondPlaceIntitial = lines[12]
    secondPlaceScore = float(lines[14])

    thirdPlaceIntitial = lines[20]
    thirdPlaceScore = float(lines[22])

    fourthPlaceIntitial = lines[28]
    fourthPlaceScore = float(lines[30])

    fifthPlaceIntitial = lines[36]
    fifthPlaceScore = float(lines[38])
