
import playerStats
import random

def battle(player, enemy, enemyLevel):
    weaponDamage = 0
    armorDefense = 0
    for weapon in playerStats.equippedWeapon.values():
        weaponDamage += weapon['damage']

    for armorSlot in playerStats.equippedArmor.values():
        for armor in armorSlot.values():
            armorDefense += armor['defense']

    print(f"You are fighting {enemy}, with {len(playerStats.party['soldiers'])} men.")

    totalPartyHealth = playerStats.party['player']['health']
    index = 0

    partyMen = [
        playerStats.party['player'],
        *playerStats.party['soldiers'].values()
    ]

    enemyMen = []

    for i in range(enemy):
        enemyMen.append({
            "health": 100,
            "attack": random.randint(3,5) * enemyLevel
        })

    while True:
        print(f"\nBattle round {index + 1}")

        if index < 1:
            print("The fight is about to begin...")
            print(f"You are about to fight with {len(playerStats.party['soldiers']) + 1} men")
            print(f"Your parties total health: {totalPartyHealth}")
        else:
            print(f"Your current health: {playerStats.party['player']['health']}")
            print(f"Your men: {len(playerStats.party['soldiers']) + 1}")

        input("Press enter to see results...")

        index += 1

        # Enemy attacks
        for enemyMan in enemyMen:
            if enemyMan['health'] <= 0:
                continue

            aliveMen = [man for man in partyMen if man['health'] > 0]

            if not aliveMen:
                break
            target = random.choice(aliveMen)
            damage = enemyMan['attack']

            if target is playerStats.party['player']:
                damage = max(0, damage - armorDefense)

            target['health'] = max(0, target['health'] - damage)

        # Player attacks
        aliveEnemies = [enemyMan for enemyMan in enemyMen if enemyMan['health'] > 0]

        if playerStats.party['player']['health'] > 0 and aliveEnemies:
            target = random.choice(aliveEnemies)
            playerDamage = playerStats.stats['strength'] + weaponDamage
            target['health'] = max(0, target['health'] - playerDamage)

        # Soldiers attack
        for soldier in playerStats.party['soldiers'].values():
            if soldier['health'] <= 0:
                continue

            aliveEnemies = [enemyMan for enemyMan in enemyMen if enemyMan['health'] > 0]

            if not aliveEnemies:
                break

            target = random.choice(aliveEnemies)
            target['health'] = max(0, target['health'] - soldier['attack'])

        # Calculate remaining health and enemies
        totalPartyHealth = sum(man['health'] for man in partyMen)

        enemiesLeft = len([enemyMan for enemyMan in enemyMen if enemyMan['health'] > 0])
        totalEnemyHealth = sum(enemyMan['health'] for enemyMan in enemyMen)

        print(f"\nEnemies remaining: {enemiesLeft}/{enemy}")
        print(f"Total enemy health is: {totalEnemyHealth}")
        print(f"Your party's remaining health: {totalPartyHealth}")

        if totalPartyHealth <= 0:
            print("Your party has been defeated!")
            return 'lost'

        elif enemiesLeft <= 0:
            print("You have defeated all enemies!")
            return 'won'
