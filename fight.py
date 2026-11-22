import playerStats
import random
import worldData


def getArmorPieces(armor):
    armorPieces = []

    for armorSlot in armor.values():
        if not isinstance(armorSlot, dict):
            continue

        if 'defense' in armorSlot:
            armorPieces.append(armorSlot)
        else:
            for armor in armorSlot.values():
                if isinstance(armor, dict) and 'defense' in armor:
                    armorPieces.append(armor)

    return armorPieces


def getArmorDefense(armor):
    armorDefense = 0

    for armorPiece in getArmorPieces(armor):
        if armorPiece.get('durability', 0) > 0:
            armorDefense += armorPiece['defense']

    return armorDefense


def damageArmor(armor, damage):
    durabilityDamage = max(1, damage // 10)

    for armorPiece in getArmorPieces(armor):
        if armorPiece.get('durability', 0) > 0:
            armorPiece['durability'] = max(0, armorPiece['durability'] - durabilityDamage)


def createEnemyArmor(enemyLevel):
    enemyArmor = {}
    armorSlots = ["helmet", "chestplate", "leggings", "boots"]

    for slot in armorSlots:
        armorChance = min(75, 10 + (enemyLevel * 12))

        if random.randint(1, 100) <= armorChance:
            availableArmor = []

            for item, info in worldData.avilableProducts.items():
                if info.get('type') == "armor" and info.get('slot') == slot:
                    availableArmor.append((item, info))

            if availableArmor:
                item, info = random.choice(availableArmor)

                enemyArmor[slot] = {
                    "name": item,
                    "defense": info['defense'],
                    "durability": info['durability']
                }

    return enemyArmor


def takeDamage(target, damage, armor=None):
    armorDefense = 0

    if armor is not None:
        armorDefense = getArmorDefense(armor)

    damageTaken = max(1, damage - armorDefense)
    oldHealth = target['health']
    target['health'] = max(0, target['health'] - damageTaken)
    actualDamage = oldHealth - target['health']

    if armor is not None:
        damageArmor(armor, damage)

    return actualDamage


def battle(player, enemy, enemyLevel):
    weaponDamage = 0
    playerKills = 0
    playerDamageDealt = 0

    for weapon in playerStats.equippedWeapon.values():
        weaponDamage += weapon['damage']

    playerClass = "melee"

    for weapon in playerStats.equippedWeapon.values():
        if weapon['type'] == "bow":
            playerClass = "archer"
            break
        elif weapon['type'] in ("sword", "axe"):
            playerClass = "melee"
            break

    print(f"You are fighting {enemy}, with {len(playerStats.party['soldiers']) + 1} men.")

    partyMen = []
    partyMen.append(playerStats.party['player'])

    for soldier in playerStats.party['soldiers'].values():
        partyMen.append(soldier)

    totalPartyHealth = sum(man['health'] for man in partyMen)
    index = 0

    enemyMen = []

    for i in range(enemy):
        enemyClass = random.choice(["melee", "archer"])

        enemyMen.append({
            "health": 100,
            "attack": random.randint(3, 5) * enemyLevel,
            "class": enemyClass,
            "armor": createEnemyArmor(enemyLevel)
        })

    armoredEnemies = 0

    for enemyMan in enemyMen:
        if enemyMan['armor']:
            armoredEnemies += 1

    if armoredEnemies > 0:
        print(f"{armoredEnemies} of the enemies are wearing armor.")

    while True:
        print(f"\nBattle round {index + 1}")

        if index < 1:
            print("The fight is about to begin...")
            print(f"You are about to fight with {len(partyMen)} men")
            print(f"Your parties total health: {totalPartyHealth}")
        else:
            print(f"Your current health: {playerStats.party['player']['health']}")
            print(f"Your men: {len(partyMen)}")

        input("Press enter to see results...")
        index += 1

        for enemyMan in enemyMen:
            if enemyMan['health'] <= 0:
                continue

            aliveMen = []

            for man in partyMen:
                if man['health'] > 0:
                    aliveMen.append(man)

            if not aliveMen:
                break

            aliveMelee = []

            for man in aliveMen:
                if man is playerStats.party['player']:
                    if playerClass == "melee":
                        aliveMelee.append(man)
                elif man['class'] != "archer":
                    aliveMelee.append(man)

            if aliveMelee:
                target = random.choice(aliveMelee)
            else:
                target = random.choice(aliveMen)

            if target is playerStats.party['player']:
                takeDamage(target, enemyMan['attack'], playerStats.equippedArmor)
            else:
                takeDamage(target, enemyMan['attack'])

        aliveEnemies = []

        for enemyMan in enemyMen:
            if enemyMan['health'] > 0:
                aliveEnemies.append(enemyMan)

        aliveMeleeEnemies = []

        for enemyMan in aliveEnemies:
            if enemyMan['class'] == "melee":
                aliveMeleeEnemies.append(enemyMan)

        if aliveMeleeEnemies:
            aliveEnemies = aliveMeleeEnemies

        if playerStats.party['player']['health'] > 0 and aliveEnemies:
            target = random.choice(aliveEnemies)

            playerDamage = playerStats.stats['strength'] + weaponDamage
            damageDone = takeDamage(target, playerDamage, target['armor'])

            playerDamageDealt += damageDone

            if target['health'] == 0:
                playerKills += 1

        for soldier in playerStats.party['soldiers'].values():
            if soldier['health'] <= 0:
                continue

            aliveEnemies = []

            for enemyMan in enemyMen:
                if enemyMan['health'] > 0:
                    aliveEnemies.append(enemyMan)

            aliveMeleeEnemies = []

            for enemyMan in aliveEnemies:
                if enemyMan['class'] == "melee":
                    aliveMeleeEnemies.append(enemyMan)

            if aliveMeleeEnemies:
                aliveEnemies = aliveMeleeEnemies

            if not aliveEnemies:
                break

            target = random.choice(aliveEnemies)
            takeDamage(target, soldier['attack'], target['armor'])

        survivingSoldiers = {}

        for name, soldier in playerStats.party['soldiers'].items():
            if soldier['health'] > 0:
                survivingSoldiers[name] = soldier

        playerStats.party['soldiers'] = survivingSoldiers

        partyMen = []
        partyMen.append(playerStats.party['player'])

        for soldier in playerStats.party['soldiers'].values():
            partyMen.append(soldier)

        totalPartyHealth = sum(man['health'] for man in partyMen)

        enemiesLeft = 0

        for enemyMan in enemyMen:
            if enemyMan['health'] > 0:
                enemiesLeft += 1

        totalEnemyHealth = sum(enemyMan['health'] for enemyMan in enemyMen)

        print(f"\nEnemies remaining: {enemiesLeft}/{enemy}")
        print(f"Total enemy health is: {totalEnemyHealth}")
        print(f"Your party's remaining health: {totalPartyHealth}")
        print(f"Your surviving soldiers: {len(playerStats.party['soldiers'])}")

        if totalPartyHealth <= 0:
            print("Your party has been defeated!")
            return 'lost'

        elif enemiesLeft <= 0:
            print("You have defeated all enemies!")

            earnedExperience = int(playerDamageDealt // 10) + (playerKills * 5)
            playerStats.giveXp(earnedExperience)

            print(f"You have earned {earnedExperience} XP!")

            return 'won'
