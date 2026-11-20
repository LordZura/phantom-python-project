import os
import playerStats
import random
import setup

def start():
    os.system("clear")
    print("What do you want to train?")
    print("1. Strength")
    print("2. Aim")
    print("3. Sword Skills")
    choice = input("> ")
    
    if choice == "1":
        trainStrength()
        setup.turn()


def trainStrength():
    os.system("clear")
    requiredStamina = playerStats.stats['stamina'] * 0.7
    if playerStats.playerSkills > 0:
        if playerStats.playerStamina > requiredStamina:
            previousStrength = playerStats.stats["strength"]
            playerStats.stats["strength"] *= random.uniform(1.2, 1.3)
            playerStats.playerStamina -= requiredStamina
            playerStats.playerSkills -= 1
            print("You have trained your strength!")
            print(f"{round(previousStrength)} -> {round(playerStats.stats['strength'])}")
            input("Press enter to continue...")
        else:
            print("You dont have enough stamina")
            print(f"Your current stamina is {round(playerStats.playerStamina)}, required is {round(requiredStamina)}.")
            input("Press enter to continue...")
    else:
        print("You dont have enough skills.")
        input("Press enter to continue...")