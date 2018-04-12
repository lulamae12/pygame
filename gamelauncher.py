import os
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
            if choice < 1 or choice > 2:
                print("That is not a valid choice!")
        except(ValueError):
            print("Please enter a valid number!")
def signin():
    print('test')
def CreateNew():
