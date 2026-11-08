def open_shop(player):
    print("\n=== SHOP ===")
    print("1. Health Potion (25 Gold)")
    print("2. Exit Shop")
    choice = input("Select an option: ").strip()
    if choice == '1':
        if player.gold >= 25:
            player.gold -= 25
            player.inventory.append("Health Potion")
            print("Purchased Health Potion!")
        else:
            print("Not enough gold!")
