import starterPlayer

def main():

    chosenClass = "swordsman"
    stats = starterPlayer.startingCharacter(chosenClass)

    print(f"Strength: {stats['strength']}")
    print(f"Aim: {stats['aim']}")

if __name__ == "__main__":
    main()