import random


def startingCharacter(player_class):

    if(player_class == "swordsman"):
        strength = random.randint(5,10)
        swordskills = random.randint(10,20)
        aim = random.randint(2,5)
        stamina = random.randint(30,50)
        scouting = random.randint(5,10)
    elif(player_class == "archer"):
        strength = random.randint(3,6)
        swordskills = random.randint(4,8)
        aim = random.randint(10,15)
        stamina = random.randint(30,50)
        scouting = random.randint(5,10)
    elif(player_class == "horseman"):
        strength = random.randint(3,6)
        swordskills = random.randint(10,20)
        aim = random.randint(2,5)
        stamina = random.randint(30,50)
        scouting = random.randint(5,10)
    else: 
        raise ValueError(f"Unknown class {player_class}")

    return {
        "strength": strength,
        "swordskills": swordskills,
        "aim": aim,
        "stamina": stamina,
        "scouting": scouting
    }