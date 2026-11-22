import random
import playerStats


def startingCharacter(player_class):

    if(player_class == "swordsman"):
        strength = random.randint(5,10)
        swordskills = random.randint(10,20)
        aim = random.randint(2,5)
        stamina = random.randint(30,50)
        scouting = random.randint(5,10)
        maxHealth = random.randint(95,110)
        playerStats.equippedWeapon = {
            "regularSword":{
                "type": "sword",
                "damage": 5
            }
        }
    elif(player_class == "archer"):
        strength = random.randint(3,6)
        swordskills = random.randint(4,8)
        aim = random.randint(10,15)
        stamina = random.randint(30,50)
        scouting = random.randint(5,10)
        maxHealth = random.randint(90,100)
        playerStats.equippedWeapon = {
            "regularBow":{
                "type": "bow",
                "damage": 3
            }
        }
    elif(player_class == "horseman"):
        strength = random.randint(3,6)
        swordskills = random.randint(7,15)
        aim = random.randint(2,5)
        stamina = random.randint(30,50)
        scouting = random.randint(5,10)
        maxEndurance = random.randint(70,80)
        maxHealth = random.randint(95,105)
        playerStats.equippedWeapon = {
            "regularSword": {
                "type": "sword",
                "damage": 5
            }
        }
        playerStats.mount = {
            "regularHorse": {
                "maxSpeed": random.randint(10, 14),
                "maxEndurance": maxEndurance,
                "endurance": maxEndurance,
                "recoverStrength": random.randint(70, 80),
                "maxHealth": random.randint(50, 60)
            },
        }
        playerStats.equippedMount = "regularHorse"
    else: 
        raise ValueError(f"Unknown class {player_class}")

    stats = {
        "strength": strength,
        "swordskills": swordskills,
        "aim": aim,
        "stamina": stamina,
        "scouting": scouting,
        "maxHealth": maxHealth
    }
    
    playerStats.setStats(stats)
    playerStats.playerStamina = playerStats.stats['stamina']