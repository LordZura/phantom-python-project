import os

day = 1
playerPosition = {
    "country": "Vaeloria",
    "settlement": "Asterfall"
}
mount = {

}
party = {
    "player":{
        "level": 1,
        "experience": 0,
        "moral": 100,
        "health": 100
    },
    "soldiers":{
        "soldier1":{
            "health": 100,
            "attack": 10
        },
        "soldier2":{
            "health": 100,
            "attack": 10
        },
        "soldier3":{
            "health": 100,
            "attack": 10
        },
        "soldier4":{
            "health": 100,
            "attack": 10
        },
        "soldier5":{
            "health": 100,
            "attack": 10
        },
        "soldier6":{
            "health": 100,
            "attack": 10
        },
        "soldier7":{
            "health": 100,
            "attack": 10
        },

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
    "none":{
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