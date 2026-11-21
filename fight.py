import playerStats
import random


def battle(player, enemy, enemyLevel):
    weaponDamage = 0
    armorDefense = 0
    playerKills = 0
    playerDamageDealt = 0

    for weapon in playerStats.equippedWeapon.values():
        weaponDamage += weapon['damage']

    for armorSlot in playerStats.equippedArmor.values():
        for armor in armorSlot.values():
            armorDefense += armor['defense']

    playerClass = "melee"

    for weapon in playerStats.equippedWeapon.values():
        if weapon['type'] == "bow":
            playerClass = "archer"
            break
        elif weapon['type'] == "sword":
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
            "class": enemyClass
        })

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

            damage = enemyMan['attack']

            if target is playerStats.party['player']:
                damage = max(0, damage - armorDefense)

            target['health'] = max(0, target['health'] - damage)

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
            damageDone = min(playerDamage, target['health'])

            target['health'] -= damageDone

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

            target['health'] = max(0, target['health'] - soldier['attack'])

        totalPartyHealth = sum(man['health'] for man in partyMen)

        enemiesLeft = 0

        for enemyMan in enemyMen:
            if enemyMan['health'] > 0:
                enemiesLeft += 1

        totalEnemyHealth = sum(enemyMan['health'] for enemyMan in enemyMen)

        print(f"\nEnemies remaining: {enemiesLeft}/{enemy}")
        print(f"Total enemy health is: {totalEnemyHealth}")
        print(f"Your party's remaining health: {totalPartyHealth}")

        if totalPartyHealth <= 0:
            print("Your party has been defeated!")
            return 'lost'

        elif enemiesLeft <= 0:
            print("You have defeated all enemies!")

            earnedExperience = int(playerDamageDealt // 10) + (playerKills * 5)
            playerStats.giveXp(earnedExperience)

            print(f"You have earned {earnedExperience} XP!")

            return 'won'