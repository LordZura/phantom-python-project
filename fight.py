import playerStats
import random

def battle(player, enemy, enemyLevel):
    print(f"You are fighting {enemy}, with {playerStats.party} men.")
    input(f"Press enter to see results...")

    while True:
        totalEnemyDamage = 0
        totalPlayerDamage = 0
        totalSoldiersDamage = 0
        totalEnemyHealth = enemy * 100
        totalPartyHealth = playerStats.party['player']['health']
        for soldier in playerStats.party['soldier']: 
            totalPartyHealth += soldier['health']
        
        for i in range(1, enemy + 1):
            enemyDamage = random.randint(3,5) * enemyLevel
            totalEnemyDamage += enemyDamage
        for soldier in playerStats.party['soldiers']:
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
    

