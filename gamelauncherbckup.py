from sys import exit
import os
cls = lambda: os.system('cls')
score = 0
scoreboardIdentifier = ''
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
        if len(Initials) != 3:
            print("ERROR: your intials should be 3 characters in length!")
        elif " " in Initials:
            print("ERROR: your intials may not contain spaces!")
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
def updateScoreboard(score):
    scoreboardLinesLocal = open("scoreboardLocals.txt", "r+")
    linesSL = scoreboardLinesLocal.readlines()
    firstPlaceIntitialSL = linesSL[3]
    firstPlaceScoreSL = float(linesSL[5])

    secondPlaceIntitialSL = linesSL[11]
    secondPlaceScoreSL = float(linesSL[13])

    thirdPlaceIntitialSL = linesSL[19]
    thirdPlaceScoreSL = float(linesSL[21])

    fourthPlaceIntitialSL = linesSL[27]
    fourthPlaceScoreSL = float(linesSL[29])

    fifthPlaceIntitialSL = linesSL[35]
    fifthPlaceScoreSL = float(linesSL[37])


    scoreboardLinesH = open("C:/Users/Public/Documents/SH.txt", "r+")
    linesSH = scoreboardLinesH.readlines()
    firstPlaceIntitialSH = linesSH[3]
    firstPlaceScoreSH = float(linesSH[5])

    secondPlaceIntitialSH = linesSH[11]
    secondPlaceScoreSH = float(linesSH[13])

    thirdPlaceIntitialSH = linesSH[19]
    thirdPlaceScoreSH = float(linesSH[21])

    fourthPlaceIntitialSH = linesSH[27]
    fourthPlaceScoreSH = float(linesSH[29])

    fifthPlaceIntitialSH = linesSH[35]
    fifthPlaceScoreSH = float(linesSH[37])

    if float(score) > firstPlaceScoreSL and  float(score) > secondPlaceScoreSL and float(score) > thirdPlaceScoreSL  and float(score) > fourthPlaceScoreSL and float(score) > fifthPlaceScoreSL:
        scoreboard_local = open("scoreboardLocals.txt","w")
        scoreboard_hardcode = open("C:/Users/Public/Documents/SH.txt","w")

        firstPlaceScoreSL = score
        firstPlaceScoreSH = score
        firstPlaceIntitialSL = scoreboardIdentifier
        firstPlaceIntitialSH = scoreboardIdentifier

        localContentTEXT = ["PLACE","\n","1ST","\n","Name1Name","\n",firstPlaceIntitialSL,"\n","Name1Score","\n",str(firstPlaceScoreSL),"\n","\n","\n",
        "PLACE","\n","2ND","\n","Name2Name","\n",secondPlaceIntitialSL,"Name2Score","\n",str(secondPlaceScoreSL),"\n","\n","\n","PLACE","\n","3RD","\n","Name3Name","\n",thirdPlaceIntitialSL,"Name3Score","\n",
        str(thirdPlaceScoreSL),"\n","\n","\n","PLACE","\n","4TH","\n","Name4Name","\n",fourthPlaceIntitialSL,"Name4Score","\n",str(fourthPlaceScoreSL),"\n","\n","\n","PLACE","\n","5TH","\n","Name5Name","\n",
        fifthPlaceIntitialSL,"Name5Score","\n",str(fifthPlaceScoreSL),"\n","\n","\n",]

        hardcodedContentTEXT = ["PLACE","\n","1ST","\n","Name1Name","\n",firstPlaceIntitialSH,"\n","Name1Score","\n",str(firstPlaceScoreSH),"\n","\n","\n",
        "PLACE","\n","2ND","\n","Name2Name","\n",secondPlaceIntitialSH,"Name2Score","\n",str(secondPlaceScoreSH),"\n","\n","\n","PLACE","\n","3RD","\n","Name3Name","\n",thirdPlaceIntitialSH,"Name3Score","\n",
        str(thirdPlaceScoreSH),"\n","\n","\n","PLACE","\n","4TH","\n","Name4Name","\n",fourthPlaceIntitialSH,"Name4Score","\n",str(fourthPlaceScoreSH),"\n","\n","\n","PLACE","\n","5TH","\n","Name5Name","\n",
        fifthPlaceIntitialSH,"Name5Score","\n",str(fifthPlaceScoreSH),"\n","\n","\n",]
        scoreboard_local.writelines(localContentTEXT)
        scoreboard_hardcode.writelines(hardcodedContentTEXT)
        scoreboard_local.close()
        scoreboard_hardcode.close()
    if float(score) < firstPlaceScoreSL and  float(score) > secondPlaceScoreSL and float(score) > thirdPlaceScoreSL  and float(score) > fourthPlaceScoreSL and float(score) > fifthPlaceScoreSL:
        scoreboard_local = open("scoreboardLocals.txt","w")
        scoreboard_hardcode = open("C:/Users/Public/Documents/SH.txt","w")

        secondPlaceScoreSL = score
        secondPlaceScoreSH = score
        secondPlaceIntitialSL = scoreboardIdentifier
        secondPlaceIntitialSH = scoreboardIdentifier

        localContentTEXT = ["PLACE","\n","1ST","\n","Name1Name","\n",firstPlaceIntitialSL,"\n","Name1Score","\n",str(firstPlaceScoreSL),"\n","\n","\n",
        "PLACE","\n","2ND","\n","Name2Name","\n",secondPlaceIntitialSL,"Name2Score","\n",str(secondPlaceScoreSL),"\n","\n","\n","PLACE","\n","3RD","\n","Name3Name","\n",thirdPlaceIntitialSL,"Name3Score","\n",
        str(thirdPlaceScoreSL),"\n","\n","\n","PLACE","\n","4TH","\n","Name4Name","\n",fourthPlaceIntitialSL,"Name4Score","\n",str(fourthPlaceScoreSL),"\n","\n","\n","PLACE","\n","5TH","\n","Name5Name","\n",
        fifthPlaceIntitialSL,"Name5Score","\n",str(fifthPlaceScoreSL),"\n","\n","\n",]

        hardcodedContentTEXT = ["PLACE","\n","1ST","\n","Name1Name","\n",firstPlaceIntitialSH,"\n","Name1Score","\n",str(firstPlaceScoreSH),"\n","\n","\n",
        "PLACE","\n","2ND","\n","Name2Name","\n",secondPlaceIntitialSH,"Name2Score","\n",str(secondPlaceScoreSH),"\n","\n","\n","PLACE","\n","3RD","\n","Name3Name","\n",thirdPlaceIntitialSH,"Name3Score","\n",
        str(thirdPlaceScoreSH),"\n","\n","\n","PLACE","\n","4TH","\n","Name4Name","\n",fourthPlaceIntitialSH,"Name4Score","\n",str(fourthPlaceScoreSH),"\n","\n","\n","PLACE","\n","5TH","\n","Name5Name","\n",
        fifthPlaceIntitialSH,"Name5Score","\n",str(fifthPlaceScoreSH),"\n","\n","\n",]
        scoreboard_local.writelines(localContentTEXT)
        scoreboard_hardcode.writelines(hardcodedContentTEXT)
        scoreboard_local.close()
        scoreboard_hardcode.close()
    scoreboardLinesLocal.close()
    scoreboardLinesH.close()
