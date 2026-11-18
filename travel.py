import worldData

def travel():
    countries = list(worldData.world.keys())

    while True:
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
        print("Choose a settlement:")

        for number, settlement in enumerate(settlements, start=1):
            print(f"{number}. {settlement}")

        choice = input("> ")

        if not choice.isdigit():
            print("Please enter a number!")
            continue

        choice = int(choice)

        if 1 <= choice <= len(settlements):
            chosen_settlement = settlements[choice - 1]
            break
        else:
            print("Invalid choice!")

        
    print(f"You have chosen your destination, {chosen_settlement} in {chosen_country}")
    print("Continue?")
    print("1. yes")
    print("2. no")
    input("> ")
