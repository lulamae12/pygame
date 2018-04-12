import os
cls = lambda: os.system('cls')
#make functiion return
def signinMenu():
    while True:
        print("Please select a choice:")
        print("╔═════════════════════════╗")
        print("║ Please select a choice: ║")
        print("║ 1. Sign in.             ║")
        print("║ 2. Create a new user    ║")
        print("╚═════════════════════════╝")
        try:
            choice = int(input())
            if choice == 1:

                signin()
                break
            if choice == 2:
                print('Create')
                CreateNew()
            if choice < 1 or choice > 2:
                print("That is not a valid choice!")
        except(ValueError):
            print("Please enter a valid number!")
def signin():
    cls()
    print('test')
def CreateNew():
    lengthOk = False
    noOddChar = False
    NameConfDone = False
    Usernames = open("usernames","a+")
    UsernamesRead = open("usernames","r")
    if UsernamesRead.mode == "r":
        UsernamesContent = UsernamesRead.read()

    cls()
    while True:
        print("╔═════════════════════════╗")
        print("║ Create a new user       ║")
        print("╚═════════════════════════╝")
        while lengthOk == False and noOddChar == False:
            print("\nplease enter your username.(This will be used to import your playerdata file so \nplease make sure its easy to remeber and dont add special characters! Example: 'DebtKillerDaveRamsey12')")
            newname = input("Username:")
            print("\n")
            if len(newname) > 15:
                print("ERROR: that name is too long! please keep it under 1O characters in length.")
            elif newname in UsernamesContent:
                print("ERROR: that username already exsists!")
            elif len(newname) < 3:
                print("ERROR: The Username has to at least have 3 characters in it.")
            elif "." in newname or "\\"  in newname:
                print("ERROR: The Username cannot have special characters")
                noOddChar = True
            elif len(newname) < 16 and len(newname) > 2:
                lenghtOk = True
                noOddChar = True
            else:
                print("ERROR: The Username may not have spaces or numbers in it.")
        if lenghtOk == True and noOddChar == True:
            while NameConfDone != True:
                print(newname,"is your name. do you want to confirm this? you cannot change it later.")
                NameConf = input("Answer(y, n):")
                if NameConf == "y":
                    print("Confirmed!")

                    Usernames.write(f"\nUsername:{str(newname)}")
                    NameConfDone = True
                    Usernames.close()

                    CreateNewScoreboard()#makes new scoreboard name
                    break
                elif NameConf == "n":
                    print("ok, returning to menu")
                    lenghtOk = False
                    noOddChar = False
                    break
                elif NameConf != "n"  and NameConf != "y":
                    print("ERROR: That is not a valid answer!")
def CreateNewScoreboard():
    scoreboardlen = False
    scoreboardSB = False#allows no odd characters
    SBConfDone = False
    scoreboardNames = open("scoreboardNames","a+")
    scoreboardNamesRead = open("scoreboardNames","r")
    if scoreboardNamesRead.mode == "r":
        scoreboardNamesContent = scoreboardNamesRead.read()

    cls()
    while scoreboardlen == False and scoreboardSB == False:
        print("\nplease enter something that will represent you on the leaderboard.\n(please keep it short(under 3 characters) and dont add spaces! Example: 'TLS')")
        newScoreboardName = input("Scoreboard name:")
        print("\n")
        if len(newScoreboardName) > 4:
            print("\nERROR: that is too long! please keep it under 4 characters in length.")
        elif newScoreboardName in scoreboardNamesContent:
             print("ERROR: that already exsists!")
        elif len(newScoreboardName) == 3:
            scoreboardlen = True
            scoreboardSB = True
        elif len(newScoreboardName) < 3:
            print("\nERROR: it has to have 3 characters in it.")

        if scoreboardSB == True and scoreboardlen == True:
            while SBConfDone != True:
                print(newScoreboardName,"will be your name on the scoreboard. Do you want to confirm this? You cannot change it later.")
                SBNameConf = input("Answer(y, n):")
                if SBNameConf == "y":

                    print("Confirmed!")
                    scoreboardNames.write(f"\nScoreBoardName:{str(newScoreboardName)}")
                    SBConfDone = True
                    scoreboardNames.close()
                    print('test')
                    break
                elif SBNameConf == "n":
                    print("ok, returning to menu")
                    scoreboardlen = False
                    scoreboardSB = False
                    break
                elif SBNameConf != "n"  and SBNameConf != "y":
                    print("ERROR: That is not a valid answer!")
