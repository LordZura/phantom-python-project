import os

day = "1"
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