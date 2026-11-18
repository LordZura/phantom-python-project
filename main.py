import starterPlayer
import setup

def main():
    chosenClass = setup.startGame()
    stats = starterPlayer.startingCharacter(chosenClass)
    setup.startGame2(stats)
if __name__ == "__main__":
    main()