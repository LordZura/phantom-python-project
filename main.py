
import starterPlayer
import setup
import worldData

def main():
    setup.introduce()
    setup.startGame()
    setup.showStats()
    worldData.setupMarket()
    worldData.setupRecruits()
    setup.turn()

if __name__ == "__main__":
    main()
