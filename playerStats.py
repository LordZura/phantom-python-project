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

equipptedArmor = {
    "helmet": "none",
    "chestplate": "none",
    "leggings": "none",
    "boots": "none"
}


def setStats(statsValue):
    global stats
    stats = statsValue

def getStats(statsValue):
    return stats[statsValue]