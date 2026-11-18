from random import choices
import os
import playerStats

def introduce():
    print("Welcome to The Wolrd Beyond")
    print("Press any key to continue.")
    choice = input("> ")
    
def startGame():
    while True:
        os.system("clear")
        print("Please Select Your Class:")
        print("1. Swordsman")
        print("2. Archer")
        print("3. Horseman")
        global classChoice
        choice = input("> ")
        if choice == "1":
            classChoice = "swordsman"
            return "swordsman"
        elif choice == "2":
            classChoice = "archer"
            return "archer"
        elif choice == "3":
            classChoice = "horseman"
            return "horseman"
        else: 
            print(f"Invalid class {choice}, please try again")
def startGame2():
    os.system("clear")
    print(f"You have chosen '{classChoice}', your stats are:")
    print(f"Strength: {playerStats.stats['strength']}")
    print(f"Swordfight Skills: {playerStats.stats['swordskills']}")
    print(f"Aim: {playerStats.stats['aim']}")
    print(f"Stamina: {playerStats.stats['stamina']}")
    print(f"Scouting: {playerStats.stats['scouting']}")