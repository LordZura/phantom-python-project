import playerStats
import random

def battle(player, enemy, enemyLevel):
    print(f"You are fighting {enemy}, with {len(playerStats.party['soldiers'])} men.")

    totalEnemyDamage = 0
    totalPlayerDamage = 0
    totalSoldiersDamage = 0
    totalEnemyHealth = enemy * 100
    totalPartyHealth = playerStats.party['player']['health']
    index = 0

    partyMen = {
        playerStats.party['player'],
        *playerStats.party['soldiers'].value()
    }

    while True:
        if index < 1:
            print("The fight is about to begin...")
            input("Press enter to see results...")
        else:
            print(f"You have finished first fight, your current health is {playerStats.party['player']['health']}, your men are {len(playerStats.party['soldiers'])}")
            input("Press enter to see results of the upcoming fight...")
        
        index += 1

        for soldier in playerStats.party['soldiers'].values(): 
            totalPartyHealth += soldier['health']
        
        for i in range(1, enemy + 1):
            enemyDamage = random.randint(3,5) * enemyLevel
            totalEnemyDamage += enemyDamage
        for soldier in playerStats.party['soldiers'].values():
            totalSoldiersDamage += soldier['attack']
        totalPlayerDamage = playerStats.stats["strength"]

        totalAttackDamage = totalPlayerDamage + totalSoldiersDamage 
        totalEnemyHealth -= totalAttackDamage
        totalPartyHealth -= totalEnemyDamage
        
        if totalPartyHealth <= 0:
            return 'lost'
        elif totalEnemyHealth <= 0:
            return 'won'
        else:
            continue
