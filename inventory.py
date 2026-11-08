def manage_inventory(player):
    print("\n=== INVENTORY ===")
    if not player.inventory:
        print("Your inventory is empty.")
        return
    
    for idx, item in enumerate(player.inventory, 1):
        print(f"{idx}. {item}")
    
    choice = input("Select an item to use or type '0' to go back: ").strip()
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(player.inventory):
            item_used = player.inventory[idx]
            if "Potion" in item_used:
                player.inventory.pop(idx)
                player.hp = min(player.max_hp, player.hp + 30)
                print(f"Used {item_used}. Restored 30 HP!")
            else:
                print(f"You cannot use {item_used} right now.")
