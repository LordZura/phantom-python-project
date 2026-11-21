import random


world = {
    "Vaeloria": {
        "Asterfall": (400, 640),
        "Windmere": (520, 700),
        "Elderglen": (550, 560),
        "Thornwick": (350, 500),
        "Larkhaven": (270, 590)
    },

    "Dravenn": {
        "Blackridge": (1100, 840),
        "Varghelm": (1250, 920),
        "Ironhollow": (1200, 750),
        "Duskmere": (1020, 720),
        "Grimwatch": (1330, 810)
    },

    "Elarune": {
        "Moonveil": (1100, 430),
        "Silverbloom": (1250, 520),
        "Lunaris": (1350, 380),
        "Evermist": (1160, 300),
        "Starhollow": (1280, 250)
    },

    "Kharvoss": {
        "Ashenford": (650, 260),
        "Dreadmoor": (800, 200),
        "Cinderwatch": (950, 260),
        "Volkrath": (760, 100),
        "Emberfall": (570, 140)
    },

    "Myrthalen": {
        "Willowshade": (180, 930),
        "Briarwood": (320, 1000),
        "Greenhollow": (420, 890),
        "Mossreach": (260, 800),
        "Fernvale": (120, 850)
    },

    "Solmere": {
        "Suncrest": (780, 650),
        "Goldhaven": (900, 700),
        "Brightwater": (950, 570),
        "Dawnspire": (800, 520),
        "Summerholt": (680, 590)
    },

    "Odravia": {
        "Ravenport": (650, 1020),
        "Frosthaven": (800, 1080),
        "Crowmere": (930, 990),
        "Hollowpeak": (790, 900),
        "Winterhold": (600, 920)
    }
}

market = {
    "Vaeloria": {
        "budget": 0,
        "products": {

        }
    },

    "Dravenn": {
        "budget": 0,
        "products": {
            
        }
    },

    "Elarune": {
        "budget": 0,
        "products": {
            
        }
    },

    "Kharvoss": {
        "budget": 0,
        "products": {
            
        }
    },

    "Myrthalen": {
        "budget": 0,
        "products": {
            
        }
    },

    "Solmere": {
        "budget": 0,
        "products": {
            
        }
    },

    "Odravia": {
        "budget": 0,
        "products": {
            
        }
    }
}
recruits = {
    "Vaeloria": {
        "products": {

        }
    },

    "Dravenn": {
        "products": {
            
        }
    },

    "Elarune": {
        "products": {
            
        }
    },

    "Kharvoss": {
        "products": {
            
        }
    },

    "Myrthalen": {
        "products": {
            
        }
    },

    "Solmere": {
        "products": {
            
        }
    },

    "Odravia": {
        "products": {
            
        }
    }
}


avilableProducts = {
    "salt":{
        "count": (100,500),
        "cost": (2,5)
    },
    "wood":{
        "count": (50,150),
        "cost": (5,15)
    },
    "iron":{
        "count": (10,150),
        "cost": (35,120)
    },
    "food":{
        "count": (200,800),
        "cost": (3,10)
    },
}

avilableRecruits = {
    "rookie swordsman":{
        "count": (5,10),
        "cost": (50,60),
        "level": 1,
        "class": "melee"
    },
    "experienced swordsman":{
        "count": (3,8),
        "cost": (110,130),
        "level": 2,
        "class": "melee"
    },
    "elite swordsman":{
        "count": (1,4),
        "cost": (200,250),
        "level": 3,
        "class": "melee"
    },
    "archer":{
        "count": (4,9),
        "cost": (60,70),
        "level": 1,
        "class": "archer"
    },
    "elite archer":{
        "count": (1,3),
        "cost": (250,260),
        "level": 3,
        "class": "archer"
    },
    
}


def setupMarket():
    for country in market.values():
        country['budget'] = random.randint(5000, 15000)
        country['products'] = {}

        for product, info in avilableProducts.items():
            if random.random() < 0.75:
                country["products"][product] = {
                    "count": random.randint(*info["count"]),
                    "cost": random.randint(*info["cost"])
                }

def setupRecruits():
    for country in recruits.values():
        country['products'] = {}

        for product, info, in avilableRecruits.items():
            if random.random() < 0.75:
                country["products"][product] = {
                    "count": random.randint(*info["count"]),
                    "cost": random.randint(*info["cost"]),
                    "level": info['level'],
                    "class": info['class']
                }