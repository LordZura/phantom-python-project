from random import choices
import os
import playerStats
import travel
import starterPlayer
import train
import traven
import tournament

def introduce():
    print("Welcome to The Wolrd Beyond`")
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
            starterPlayer.startingCharacter(classChoice)
            return "swordsman"
        elif choice == "2":
            classChoice = "archer"
            starterPlayer.startingCharacter(classChoice)
            return "archer"
        elif choice == "3":
            classChoice = "horseman"
            starterPlayer.startingCharacter(classChoice)
            return "horseman"
        else: 
            print(f"Invalid class {choice}, please try again")

def showStats():
    os.system("clear")
    print(f"You have chosen '{classChoice}', your stats are:")
    print(f"Strength: {playerStats.stats['strength']}")
    print(f"Swordfight Skills: {playerStats.stats['swordskills']}")
    print(f"Aim: {playerStats.stats['aim']}")
    print(f"Stamina: {playerStats.stats['stamina']}")
    print(f"Scouting: {playerStats.stats['scouting']}")
    print("Press anything to continue.")
    choice = input("> ")
    
def turn():
    while True:
        os.system("clear")
        print(f"Day {playerStats.day}, Location {playerStats.playerPosition['settlement']} in {playerStats.playerPosition['country']} What is your action?")
        print("1. Travel")
        print("2. Train")
        print("3. Inventory")
        print("4. Check Stats")
        print("5. Traven")
        print("6. Enter Tournament")
        print("7. Exit the game. (for now nothing is saved :D)")
        choice = input("> ")

        if choice == "1":
            travel.Starttravel()
        elif choice == "2":
            train.start()
        elif choice == "3":
            playerStats.inventoryMenu()
        elif choice == "4":
            playerStats.displayStats()
        elif choice == "5":
            traven.openTraven()
        elif choice == "6":
            tournament.enter()
        elif choice == "7":
            exit()


def lost():
    print("You have lost... yeah, you died. Game over.")
    input("Press enter to quit the game.")
    exit()
