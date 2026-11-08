import random

def start_combat(player, monster):
    print(f"\n[ALERT] A wild {monster.name} appears!")
    while monster.hp > 0 and player.hp > 0:
        print(f"\nYour HP: {player.hp} | {monster.name} HP: {monster.hp}")
        action = input("1. Attack\n2. Use Potion\n3. Run\nChoose: ").strip()
        if action == '1':
            dmg = random.randint(10, 20)
            monster.hp -= dmg
            print(f"You struck {monster.name} for {dmg} damage.")
        elif action == '2' and "Health Potion" in player.inventory:
            player.inventory.remove("Health Potion")
            player.hp = min(player.max_hp, player.hp + 30)
            print("You used a Health Potion.")
        elif action == '3':
            print("You fled from combat!")
            return False
        
        if monster.hp > 0:
            player.hp -= monster.attack
            print(f"{monster.name} attacks you for {monster.attack} damage.")
    
    if player.hp <= 0:
        print("You were defeated...")
        return False
    else:
        print(f"[VICTORY] You defeated {monster.name}! Earned {monster.xp_reward} XP and {monster.gold_reward} gold.")
        player.xp += monster.xp_reward
        player.gold += monster.gold_reward
        return True