
import random
import os
import playerStats


def enter():
    os.system('clear')
    print("You are about to enter the tournament")
    print("You will face 9 great warriors")
    print("Do you want to enter the tournament?")
    print("1. yes")
    print("2. no")

    choice = input("> ")

    if choice == "1":
        opponents = generateWarriors()
        battle(opponents)
    elif choice == "2":
        return
    else:
        print("Invalid choice.")
        enter()


def battle(opponents):
    currentEnemy = 0
    assignedHealth = playerStats.stats['maxHealth']
    os.system("clear")

    while currentEnemy < len(opponents) and assignedHealth > 0:

        enemyHealth = opponents[currentEnemy]['health']
        enemyAttack = opponents[currentEnemy]['attack']
        enemySwordskills = opponents[currentEnemy]['swordskills']
        assignedHealth = playerStats.stats['maxHealth']

        print("\nYou are facing your opponent...")

        while enemyHealth > 0 and assignedHealth > 0:
            enemyHealth, assignedHealth = attackTurn(
                enemyHealth, enemyAttack, enemySwordskills, assignedHealth
            )

        if assignedHealth <= 0:
            lose()
            return

        print("\nYou have beaten your opponent...")
        currentEnemy += 1

        if currentEnemy < len(opponents):
            os.system('clear')
            print("You are now facing your next opponent...")
            input("Press enter to continue...")

    if currentEnemy == len(opponents):
        win()
        prize()


def generateWarriors():
    opponents = []

    for i in range(9):
        opponent = {
            "health": random.randint(100, 130),
            "attack": random.randint(15, 30),
            "swordskills": random.randint(15, 40),
            "position": i
        }

        opponents.append(opponent)

    return opponents


def attackTurn(enemyHealth, enemyAttack, enemySwordskills, assignedHealth):
    os.system("clear")
    print("\nChoose your strategy:")
    print("1. Charge without thinking")
    print("2. Be defensive")
    print("3. Be offensive")

    choice = input("> ")

    if choice == "1":
        return charge(enemyHealth, enemyAttack, enemySwordskills, assignedHealth)
    elif choice == "2":
        return defensive(enemyHealth, enemyAttack, enemySwordskills, assignedHealth)
    elif choice == "3":
        return offensive(enemyHealth, enemyAttack, enemySwordskills, assignedHealth)
    else:
        print("Invalid choice.")
        return enemyHealth, assignedHealth


def charge(enemyHealth, enemyAttack, enemySwordskills, assignedHealth):
    os.system("clear")
    weaponDamage = next(iter(playerStats.equippedWeapon.values()))["damage"]

    playerDamage = playerStats.stats['strength'] + weaponDamage
    enemyDamage = enemyAttack + enemySwordskills // 10

    enemyHealth -= playerDamage

    if enemyHealth > 0:
        assignedHealth -= enemyDamage
    else:
        enemyDamage = 0

    print("\nYou have charged into the enemy...")
    print(f"You have dealt {playerDamage}, and received {enemyDamage}")
    print(f"Your health: {assignedHealth}")
    print(f"Enemy health: {max(0, enemyHealth)}")

    input("Press enter to continue...")

    return enemyHealth, assignedHealth


def defensive(enemyHealth, enemyAttack, enemySwordskills, assignedHealth):
    os.system('clear')
    weaponDamage = next(iter(playerStats.equippedWeapon.values()))["damage"]

    playerDamage = playerStats.stats['strength'] + weaponDamage // 2
    enemyDamage = (enemyAttack + enemySwordskills // 10) // 2

    enemyHealth -= playerDamage

    if enemyHealth > 0:
        assignedHealth -= enemyDamage
    else:
        enemyDamage = 0

    print("\nYou are carefully defending yourself...")
    print(f"You have dealt {playerDamage}, and received {enemyDamage}")
    print(f"Your health: {assignedHealth}")
    print(f"Enemy health: {max(0, enemyHealth)}")

    input("Press enter to continue...")

    return enemyHealth, assignedHealth


def offensive(enemyHealth, enemyAttack, enemySwordskills, assignedHealth):
    os.system('clear')
    weaponDamage = next(iter(playerStats.equippedWeapon.values()))["damage"]

    playerDamage = playerStats.stats['strength'] + weaponDamage + 10
    enemyDamage = enemyAttack + enemySwordskills // 10

    enemyHealth -= playerDamage

    if enemyHealth > 0:
        assignedHealth -= enemyDamage
    else:
        enemyDamage = 0

    print("\nYou are attacking aggressively...")
    print(f"You have dealt {playerDamage}, and received {enemyDamage}")
    print(f"Your health: {assignedHealth}")
    print(f"Enemy health: {max(0, enemyHealth)}")

    input("Press enter to continue...")

    return enemyHealth, assignedHealth


def lose():
    os.system('clear')
    print("\nYou have lost...")
    input("Press enter to exit the tournament.")


def win():
    os.system('clear')
    print("\nYou have beaten all 9 warriors!")
    print("You are the tournament champion!")


def prize():
    os.system('clear')
    reward = 5000
    playerStats.gold += reward

    print(f"\nYou have received {reward} gold!")
    print(f"Your current gold: {playerStats.gold}")
    input("Press enter to continue...")
