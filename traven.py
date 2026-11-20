import worldData
import playerStats

def openTraven():
    print("You entered the market, what do you want to buy?")
    print("1. Market")
    print("2. Recruits")

    choice = input("> ")

    if choice == "1":
        openMarket()


def openMarket():

    country = playerStats.playerPosition["country"]
    countryMarket = worldData.market[country]

    products = countryMarket["products"]

    print(f"\n{country} Market")
    print(f"Market budget: {countryMarket['budget']} gold\n")

    for product, info in products.items():
        print(f"{product.capitalize()}")
        print(f"  Stock: {info['count']}")
        print(f"  Price: {info['cost']} gold each")
        print("")

    print("Choose which one you want to buy, and how much.")
