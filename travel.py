import setup
import playerStats
import starterPlayer
import worldData
import os
from math import dist
import random
import fight


def Starttravel():
    countries = list(worldData.world.keys())

    while True:  # Go back to country selection

        while True:
            os.system("clear")
            print("Choose a country:")

            for number, country in enumerate(countries, start=1):
                print(f"{number}. {country}")

            choice = input("> ")

            if not choice.isdigit():
                print("Please enter a number!")
                continue

            choice = int(choice)

            if 1 <= choice <= len(countries):
                chosen_country = countries[choice - 1]
                break
            else:
                print("Invalid choice!")

        settlements = worldData.world[chosen_country]

        current_position = worldData.world[
            playerStats.playerPosition["country"]
        ][playerStats.playerPosition["settlement"]]

        chosen_settlement = None

        while True:
            os.system("clear")
            print("Choose a settlement:")

            settlement_names = list(settlements.keys())

            for number, settlement in enumerate(settlement_names, start=1):
                distance = dist(current_position, settlements[settlement])
                print(f"{number}. {settlement} - {distance:.1f}km")

            print(f"{len(settlements) + 1}. Back <-")

            choice = input("> ")

            if not choice.isdigit():
                print("Please enter a number!")
                continue

            choice = int(choice)

            if 1 <= choice <= len(settlements):
                chosen_settlement = settlement_names[choice - 1]
                break
            elif chosen_settlement is None:
                break
            else:
                print("Invalid choice!")

        if chosen_settlement is None:
            continue

        break

    destination = worldData.world[chosen_country][chosen_settlement]
    calcuated_distance = dist(current_position, destination)


    while True:

        os.system("clear")
        print(f"You have chosen your destination, {chosen_settlement} in {chosen_country}")
        print(f"Distance is {calcuated_distance:.1f}km")
        print("Continue?")
        print("1. yes")
        print("2. no")
        choice = input("> ")
        if choice == "1":
            if playerStats.equippedMount == 0:
                travelOnFoot(playerStats.stats['scouting'], calcuated_distance)
            else:
                horseStats = playerStats.mount[playerStats.equippedMount]
                travel(horseStats, calcuated_distance)

            playerStats.playerPosition['country'] = chosen_country
            playerStats.playerPosition['settlement'] = chosen_settlement

            print(f"Welcome to {chosen_settlement}, in {chosen_country}")
            setup.turn()
            break
        elif choice == "2":
            setup.turn()
        else:
            print("Please select either 1 or 2.")
    
    
def travelDay(horse, remaining_distance):


    todaysDistance = min(remaining_distance, horse['endurance'])



    hours = todaysDistance / horse['maxSpeed']

    horse['endurance'] -= todaysDistance

    return todaysDistance, hours

def restDay(horse):
    horse["endurance"] += horse["recoverStrength"]

    if horse["endurance"] > horse["maxEndurance"]:
        horse["endurance"] = horse["maxEndurance"]

    
def travel(horse, total_distance):
    remaining = total_distance
    day = 0

    while remaining > 0:
        daysChunk = 0


        while remaining > 0 and daysChunk < 10:
            day += 1
            daysChunk += 1
            playerStats.day = int(playerStats.day) + 1

            if horse["endurance"] > 0:
                distance, hours = travelDay(horse, remaining)
                remaining -= distance
                print(f"Day {day}: traveled {distance}km ({hours:.1f}h), {remaining}km left")
            else:
                restDay(horse)
                print(f"Day {day}: resting, endurance now {horse['endurance']}")

            if remaining <= 0:
                break
        if remaining > 0:
            encounter()
            input("\nPress enter to continue the next 10 days of travel...")

    print(f"\nArrived in {day} days!") 
    input("Press anything to continue...")


def travelOnFoot(scouting, total_distance):
    
    kmDay = 15 + (scouting * 2)

    remaining = total_distance
    day = 0

    while remaining > 0:
        daysChunk = 0

        while remaining > 0 and daysChunk < 10:
            day += 1    
            daysChunk += 1
            playerStats.day = int(playerStats.day) + 1

            todaysDistance = min(remaining, kmDay)
            remaining -= todaysDistance
            print(f"Day {day}: walked {todaysDistance}km, {remaining}km left")

            if remaining <= 0:
                break

        if remaining > 0:
            encounter()
            input("\nPress enter to continue next 10 days of walking...")
            

    print(f"\nArrived on foot in {day} days!")
    input("Press any key to continue...")


def encounter():
    chance = random.randint(1, 100) + (playerStats.stats['scouting'])
    if chance <= 30:
        print("You have been ambushed!")
        enemy = random.randint(3, 10)
        enemyLevel = random.randint(1, 5)
        outcome = fight.battle(0, enemy, enemyLevel)
        if outcome == 'lost':
            setup.lost()
        elif outcome == 'won':
            gold = random.randint(100, 300)
            print(f"You recieved: {gold} gold")
            input("Press enter to continue your journey...")
    