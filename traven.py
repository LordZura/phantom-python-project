
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
            print("Recruitment is not available yet.")
            input("Press enter to continue...")

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

        # Remove the gold from the player
        playerStats.gold -= totalCost

        # Remove products from the market
        info["count"] -= amount

        # Add products to the player's inventory
        if selectedProduct not in playerStats.inventory:
            playerStats.inventory[selectedProduct] = 0

        playerStats.inventory[selectedProduct] += amount

        print(f"\nSuccessfully bought {amount} {selectedProduct}!")
        print(f"Remaining gold: {playerStats.gold}")

        input("\nPress enter to continue...")
