
import worldData
import playerStats


def openTraven():
    while True:
        print("\nYou entered the market. What do you want to do?")
        print("1. Market")
        print("2. Recruits")
        print("3. Leave")

        choice = input("> ")

        if choice == "1":
            openMarket()

        elif choice == "2":
            reqruit()

        elif choice == "3":
            return

        else:
            print("Invalid choice!")


def openMarket():
    country = playerStats.playerPosition["country"]
    countryMarket = worldData.market[country]
    products = countryMarket["products"]

    while True:
        print(f"\n========== {country} Market ==========")
        print(f"Your gold: {playerStats.gold} gold")
        print(f"Market budget: {countryMarket['budget']} gold\n")

        if not products:
            print("There are currently no products available.")
            input("Press enter to go back...")
            return

        productNames = list(products.keys())

        for number, product in enumerate(productNames, start=1):
            info = products[product]

            print(f"{number}. {product.capitalize()}")
            print(f"   Stock: {info['count']}")
            print(f"   Price: {info['cost']} gold each")

        print("\n0. Go back")
        print("\nChoose a product:")

        choice = input("> ")

        if choice == "0":
            return

        if not choice.isdigit():
            print("Please enter a number!")
            continue

        choice = int(choice)

        if choice < 1 or choice > len(productNames):
            print("Invalid choice!")
            continue

        selectedProduct = productNames[choice - 1]
        info = products[selectedProduct]

        print(f"\nHow many {selectedProduct} do you want to buy?")
        amount = input("> ")

        if not amount.isdigit():
            print("Please enter a valid amount!")
            continue

        amount = int(amount)

        if amount <= 0:
            print("You must buy at least 1.")
            continue

        if amount > info["count"]:
            print("The market doesn't have enough stock!")
            continue

        totalCost = amount * info["cost"]

        print(f"\nProduct: {selectedProduct.capitalize()}")
        print(f"Amount: {amount}")
        print(f"Total cost: {totalCost} gold")

        if totalCost > playerStats.gold:
            print("You don't have enough gold!")
            continue

        confirm = input("Confirm purchase? (y/n): ").lower()

        if confirm not in ("y", "yes"):
            print("Purchase cancelled.")
            continue

        playerStats.gold -= totalCost
        info["count"] -= amount

        if selectedProduct not in playerStats.inventory:
            playerStats.inventory[selectedProduct] = 0

        playerStats.inventory[selectedProduct] += amount

        print(f"\nSuccessfully bought {amount} {selectedProduct}!")
        print(f"Remaining gold: {playerStats.gold}")

        input("\nPress enter to continue...")


def reqruit():
    country = playerStats.playerPosition['country']
    availableRecruits = worldData.recruits[country]['products']

    while True:
        print(f"\n========== {country} Recruits ==========")
        print(f"Your gold: {playerStats.gold} gold\n")

        if not availableRecruits:
            print("There are currently no recruits available.")
            input("Press enter to go back...")
            return

        recruitNames = list(availableRecruits.keys())

        for number, recruitName in enumerate(recruitNames, start=1):
            info = availableRecruits[recruitName]

            print(f"{number}. {recruitName.capitalize()}")
            print(f"   Stock: {info['count']}")
            print(f"   Cost: {info['cost']} gold each")
            print(f"   Level: {info['level']}")
            print(f"   Class: {info['class']}")
            print("")

        print("0. Go back")
        print("Choose a recruit:")

        choice = input("> ")

        if choice == "0":
            return

        if not choice.isdigit():
            print("Please enter a number!")
            continue

        choice = int(choice)

        if choice < 1 or choice > len(recruitNames):
            print("Invalid choice!")
            continue

        selectedRecruit = recruitNames[choice - 1]
        info = availableRecruits[selectedRecruit]

        print(f"\nHow many {selectedRecruit} do you want to recruit?")
        amount = input("> ")

        if not amount.isdigit():
            print("Please enter a valid amount!")
            continue

        amount = int(amount)

        if amount <= 0:
            print("You must recruit at least 1.")
            continue

        if amount > info['count']:
            print("There are not enough recruits available!")
            continue

        totalCost = amount * info['cost']

        print(f"\nRecruit: {selectedRecruit.capitalize()}")
        print(f"Amount: {amount}")
        print(f"Total cost: {totalCost} gold")

        if totalCost > playerStats.gold:
            print("You don't have enough gold!")
            continue

        confirm = input("Confirm recruitment? (y/n): ").lower()

        if confirm not in ("y", "yes"):
            print("Recruitment cancelled.")
            continue

        playerStats.gold -= totalCost
        info['count'] -= amount

        for i in range(amount):
            soldierNumber = 1

            while f"soldier{soldierNumber}" in playerStats.party['soldiers']:
                soldierNumber += 1

            soldierName = f"soldier{soldierNumber}"

            playerStats.party['soldiers'][soldierName] = {
                "class": info['class'],
                "health": 100,
                "attack": info['level'] * 10,
                "level": info['level']
            }

        print(f"\nSuccessfully recruited {amount} {selectedRecruit}!")
        print(f"Remaining gold: {playerStats.gold}")
        print(f"Your party now has {len(playerStats.party['soldiers']) + 1} men.")

        input("\nPress enter to continue...")
