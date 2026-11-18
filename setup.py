from random import choices


def startGame():
    print("Welcome to The Wolrd Beyond")
    print("Please Select Your Class:")
    print("1. Swordsman")
    print("2. Archer")
    print("3. Horseman")
    global classChoice
    choice = input("> ")
    if choice == "1" or "Swordsman" or "swordsman":
        classChoice = "swordsman"
        return "swordsman"
    elif choice == "2" or "Archer" or "archer":
        classChoice = "archer"
        return "archer"
    elif choice == "3" or "Horseman" or "horseman":
        classChoice = "horseman"
        return "horseman"
def startGame2(stats):
    print(f"You have chosen {classChoice}, your stats are:")
    print(f"Strength: {stats['strength']}")