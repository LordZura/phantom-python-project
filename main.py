import starterPlayer
import setup

def main():
    setup.introduce()
    chosenClass = setup.startGame()
    stats = starterPlayer.startingCharacter(chosenClass)
    setup.startGame2()
if __name__ == "__main__":
    main()