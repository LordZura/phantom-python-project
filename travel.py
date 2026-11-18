import setup
import playerStats
import starterPlayer
import worldData
import os
from math import dist

def Starttravel():
    countries = list(worldData.world.keys())

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

    while True:
        os.system("clear")
        print("Choose a settlement:")
        settlement_names = list(settlements.keys())
        for number, settlement in enumerate(settlement_names, start=1):
            print(f"{number}. {settlement}")

        choice = input("> ")

        if not choice.isdigit():
            print("Please enter a number!")
            continue

        choice = int(choice)
        

        if 1 <= choice <= len(settlements):
            chosen_settlement = settlement_names[choice - 1]
            break
        else:
            print("Invalid choice!")

    
    current_position = worldData.world[
        playerStats.playerPosition["country"]
    ][playerStats.playerPosition["settlement"]]

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
        day += 1

        if horse["endurance"] > 0:
            distance, hours = travelDay(horse, remaining)
            remaining -= distance
            print(f"Day {day}: traveled {distance}km ({hours:.1f}h), {remaining}km left")
        else:
            restDay(horse)
            print(f"Day {day}: resting, endurance now {horse['endurance']}")

    print(f"\nArrived in {day} days!")


def travelOnFoot(scouting, total_distance):
    
    kmDay = 15 + (scouting * 2)

    remaining = total_distance
    day = 0

    while remaining > 0:
        day += 1
        todaysDistance = min(remaining, kmDay)
        remaining -= todaysDistance
        print(f"Day {day}: walked {todaysDistance}km, {remaining}km left")

    print(f"\nArrived on foot in {day} days!")