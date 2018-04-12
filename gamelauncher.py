import os
cls = lambda: os.system('cls')
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
    cls()
    while True:
        print("╔═════════════════════════╗")
        print("║ Create a new user       ║")
        print("╚═════════════════════════╝")
        while lengthOk == False and noOddChar == False:
            print("\nplease enter your first name and last initial.(This will be used to import your playerdata file so \nplease keep it short and dont add spaces! Example: 'DaveR')")
            newname = input("name:")
            print("\n")
            if len(newname) > 10:
                print("ERROR: that name is too long! please keep it under 1O characters in length.")
            elif len(newname) < 11 and len(newname) > 2:
                lenghtOk = True
            elif len(newname) < 3:
                print("ERROR: The name has to at least have 3 characters in it.")
            if newname.isalpha():
                noOddChar = True
            else:
                print("ERROR: The string may not have spaces or numbers in it.")
        if lenghtOk == True and noOddChar == True:
            while NameConfDone != True:
                print(newname,"is your name. do you want to confirm this? you cannot change it later.")
                NameConf = input("Answer(y, n):")
                if "y" in NameConf:
                    filename = newname #new file name
                    print("Confirmed!")
                    NameConfDone = True
                elif "n" in NameConf:
                    print("ok, returning to menu")
                    lenghtOk = False
                    noOddChar = False
                    break
                elif NameConf != "n"  and NameConf != "y":
                    print("ERROR: That is not a valid answer!")
