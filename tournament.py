
import random

import playerStats

def enter():
    print("You are about to enter the tournament")
    print("You will face 9 great warriors")
    print("Do you want to enter the tournament?")
    print("1. yes")
    print("2. no")
    choice = input("> ")

    if choice == "1":
        pass
    elif choice == "2":
        return

    opponents = generateWarrirors()
    battle(opponents)

def battle(opponents):
    currentEnemy = 0
    assignedHealth = playerStats.stats['maxHealth']

    while True:
        enemyHealth = opponents[currentEnemy]['health']
        enemyAttack = opponents[currentEnemy]['attack']
        enemySwordskills = opponents[currentEnemy]['swordskills']

        print(f"You are facing your opponent...")
        assignedHealth = attackTurn(
            enemyHealth, enemyAttack, enemySwordskills, assignedHealth
        )

def generateWarrirors():
    opponents = []

    for i in range(9):
        opponent = {
            "health": random.randint(100, 130),
            "attack": random.randint(15,30),
            "swordskills": random.randint(15,40),
            "position": i
        }

        opponents.append(opponent)
    return opponents


def attackTurn(enemyHealth, enemyAttack, enemySwordskills, assignedHealth):
    print("Choose your strategy:")
    print("1. Charge without thinking")
    print("2. Be defensive")
    print("3. Be offensive")

    choice = input("> ")

    if choice == "1":
        return charge(enemyHealth, enemyAttack, enemySwordskills, assignedHealth)
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass

def charge(enemyHealth, enemyAttack, enemySwordskills, assignedHealth):

    if assignedHealth <= 0:
        lose()
    elif enemyHealth <= 0:
        win()

    assignedHealth -= enemyAttack
    weaponDamage = next(iter(playerStats.equippedWeapon.values()))["damage"]
    playerDamage = playerStats.stats['strength'] + weaponDamage
    enemyHealth -= playerDamage

    print("You have charged into the enemy...")
    print(f"You have dealt {playerDamage}, and recieved {enemyAttack}")
    input("Press enter to continue...")

    return assignedHealth


def lose():
    print("You have lost...")
    input("Press enter to exit the tournament.")
    pass

def win():
    pass
