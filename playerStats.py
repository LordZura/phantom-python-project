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


def setStats(statsValue):
    global stats
    stats = statsValue

def getStats(statsValue):
    return stats[statsValue]