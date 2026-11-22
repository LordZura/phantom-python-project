
import os

day = 1
gold = 500
inventory = {
    "salt": 10,
    "food": 5,
    "stuff": 100
}

playerPosition = {
    "country": "Vaeloria",
    "settlement": "Asterfall"
}

mount = {

}

party = {
    "player": {
        "level": 1,
        "experience": 0,
        "moral": 100,
        "health": 100
    },
    "soldiers": {
        "soldier1": {
            "class": "melee",
            "health": 100,
            "attack": 10
        }
    }
}

equippedMount = 0

playerExperience = 0
playerLevel = 1
playerNextLevelup = 20
playerSkills = 0

equippedArmor = {
    "helmet": {
        "none": {
            "durability": 0,
            "defense": 0
        }
    },
    "chestplate": {
        "none": {
            "durability": 0,
            "defense": 0
        }
    },
    "leggings": {
        "none": {
            "durability": 0,
            "defense": 0
        }
    },
    "boots": {
        "none": {
            "durability": 0,
            "defense": 0
        }
    }
}

equippedWeapon = {
    "none": {
        "type": "sword",
        "damage": 0
    }
}

playerStamina = 0


def setStats(statsValue):
    global stats
    stats = statsValue


def getStats(statsValue):
    return stats[statsValue]


def displayStats():
    os.system("clear")
    print("Your full stats:")
    print("")
    print("Physical stats:")

    for stat, value in stats.items():
        print(f"- {stat.capitalize()}: {value}")

    print("Other:")
    print(f"Skill points: {playerSkills}")
    print("")
    input("Press enter to conitnue")


def giveXp(amount):
    global playerExperience, playerLevel, playerNextLevelup, playerSkills

    playerExperience += amount

    while playerExperience >= playerNextLevelup:
        playerExperience -= playerNextLevelup
        playerLevel += 1
        playerSkills += 1
        playerNextLevelup += 25

        print(f"You have leveled up! You are now {playerLevel}")
        print("You have gained 1 skill point")


def advanceDay():
    global day
    day += 1

    if day % 100 == 0:
        import worldData
        worldData.setupMarket()

def getInventoryCategory(item):
    import worldData

    info = worldData.avilableProducts.get(item, {})

    if info.get("type") == "weapon":
        return "weapons"
    elif info.get("type") == "armor":
        return "armor"
    else:
        return "items"


def showInventory(category):
    import worldData

    itemNames = []

    for item, amount in inventory.items():
        if amount > 0 and getInventoryCategory(item) == category:
            itemNames.append(item)

    print(f"\n========== {category.capitalize()} ==========")

    if not itemNames:
        print("You don't have anything in this category.")
        input("Press enter to continue...")
        return

    for number, item in enumerate(itemNames, start=1):
        info = worldData.avilableProducts.get(item, {})
        print(f"{number}. {item.capitalize()} x{inventory[item]}")

        if category == "weapons":
            print(f"   Type: {info.get('weaponType', 'Unknown')}")
            print(f"   Damage: {info.get('damage', 0)}")
        elif category == "armor":
            print(f"   Slot: {info.get('slot', 'Unknown')}")
            print(f"   Defense: {info.get('defense', 0)}")
            print(f"   Durability: {info.get('durability', 0)}")

    if category == "items":
        input("\nPress enter to go back...")
        return

    print("\n0. Go back")
    print("Choose something to equip:")
    choice = input("> ")

    if choice == "0":
        return

    if not choice.isdigit():
        print("Please enter a number!")
        input("Press enter to continue...")
        return

    choice = int(choice)

    if choice < 1 or choice > len(itemNames):
        print("Invalid choice!")
        input("Press enter to continue...")
        return

    selectedItem = itemNames[choice - 1]

    if category == "weapons":
        equipWeapon(selectedItem)
    elif category == "armor":
        equipArmor(selectedItem)

    input("Press enter to continue...")


def equipWeapon(item):
    import worldData

    if inventory.get(item, 0) <= 0:
        print("You don't have that weapon.")
        return

    info = worldData.avilableProducts.get(item)

    if not info or info.get("type") != "weapon":
        print("That item cannot be equipped as a weapon.")
        return

    for oldWeapon in list(equippedWeapon.keys()):
        if oldWeapon != "none":
            inventory[oldWeapon] = inventory.get(oldWeapon, 0) + 1

    equippedWeapon.clear()
    equippedWeapon[item] = {
        "type": info["weaponType"],
        "damage": info["damage"]
    }

    inventory[item] -= 1
    if inventory[item] <= 0:
        del inventory[item]

    print(f"You equipped {item}.")


def equipArmor(item):
    import worldData

    if inventory.get(item, 0) <= 0:
        print("You don't have that armor.")
        return

    info = worldData.avilableProducts.get(item)

    if not info or info.get("type") != "armor":
        print("That item cannot be equipped as armor.")
        return

    armorSlot = info["slot"]

    for oldArmor in list(equippedArmor[armorSlot].keys()):
        if oldArmor != "none":
            inventory[oldArmor] = inventory.get(oldArmor, 0) + 1

    equippedArmor[armorSlot] = {
        item: {
            "defense": info["defense"],
            "durability": info["durability"]
        }
    }

    inventory[item] -= 1
    if inventory[item] <= 0:
        del inventory[item]

    print(f"You equipped {item}.")


def showEquipped():
    print("\n========== Equipped Gear ==========")

    print("Weapons:")
    if equippedWeapon:
        for weapon, info in equippedWeapon.items():
            if weapon == "none":
                print("- None")
            else:
                print(f"- {weapon.capitalize()} ({info.get('type', 'unknown')}, {info.get('damage', 0)} damage)")
    else:
        print("- None")

    print("\nArmor:")
    for slot, armor in equippedArmor.items():
        for item, info in armor.items():
            if item == "none":
                print(f"- {slot.capitalize()}: None")
            else:
                print(f"- {slot.capitalize()}: {item.capitalize()}")
                print(f"  Defense: {info.get('defense', 0)}")
                print(f"  Durability: {info.get('durability', 0)}")

    print("\n1. Unequip weapon")
    print("2. Unequip armor")
    print("0. Go back")
    choice = input("> ")

    if choice == "1":
        for weapon in list(equippedWeapon.keys()):
            if weapon != "none":
                inventory[weapon] = inventory.get(weapon, 0) + 1
        equippedWeapon.clear()
        equippedWeapon["none"] = {"type": "sword", "damage": 0}
        print("You unequipped your weapon.")

    elif choice == "2":
        print("\nChoose an armor slot:")
        armorSlots = list(equippedArmor.keys())

        for number, slot in enumerate(armorSlots, start=1):
            print(f"{number}. {slot.capitalize()}")

        print("0. Cancel")
        slotChoice = input("> ")

        if slotChoice.isdigit():
            slotChoice = int(slotChoice)

            if 1 <= slotChoice <= len(armorSlots):
                selectedSlot = armorSlots[slotChoice - 1]

                for armor in list(equippedArmor[selectedSlot].keys()):
                    if armor != "none":
                        inventory[armor] = inventory.get(armor, 0) + 1

                equippedArmor[selectedSlot] = {
                    "none": {"durability": 0, "defense": 0}
                }
                print(f"You unequipped your {selectedSlot}.")


def inventoryMenu():
    while True:
        os.system("clear")
        print("========== Inventory ==========")
        print("1. Items")
        print("2. Weapons")
        print("3. Armor")
        print("4. Equipped gear")
        print("0. Back")

        choice = input("> ")

        if choice == "1":
            showInventory("items")
        elif choice == "2":
            showInventory("weapons")
        elif choice == "3":
            showInventory("armor")
        elif choice == "4":
            showEquipped()
            input("\nPress enter to continue...")
        elif choice == "0":
            return
        else:
            print("Invalid choice!")
            input("Press enter to continue...")


def checkInventory():
    inventoryMenu()