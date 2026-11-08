from player import Player
from map import GameMap
from combat import start_combat
from monster import Goblin, Boss
from shop import open_shop
from quest import QuestManager
from npc import talk_to_npc
from inventory import manage_inventory

def run_game(username):
    print("\n--- STORY INTRO ---")
    print("Darkness has fallen upon the realm. You step forward as the chosen adventurer...")
    
    player = Player(username)
    current_map = GameMap(player.current_map)
    quest_mgr = QuestManager(player)

    while True:
        player.view_status()
        current_map.display()
        print("\n--- MENU ---")
        print("1. Talk to NPC (Elder)")
        print("2. Visit Shop")
        print("3. Fight Monster")
        print("4. Manage Inventory")
        print("5. View Quests")
        print("6. Switch Map")
        print("7. Save & Quit")
        
        choice = input("Enter choice: ").strip()
        if choice == '1':
            talk_to_npc("Elder")
        elif choice == '2':
            open_shop(player)
        elif choice == '3':
            if player.quest_progress.get('main_quest', 0) >= 2:
                monster = Boss()
            else:
                monster = Goblin()
            
            won = start_combat(player, monster)
            if won and isinstance(monster, Boss):
                print("\nCONGRATULATIONS! You defeated the Dark Overlord and won the game!")
                break
        elif choice == '4':
            manage_inventory(player)
        elif choice == '5':
            quest_mgr.check_quests()
        elif choice == '6':
            player.current_map = 'wilderness' if player.current_map == 'town' else 'town'
            current_map = GameMap(player.current_map)
            print(f"Travelled to {player.current_map}!")
        elif choice == '7':
            player.save_data()
            print("Game saved. Goodbye!")
            break
