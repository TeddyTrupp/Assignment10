from auth import register_user, login_user
from game import run_game

def main():
    print("=== WELCOME TO TERMINAL RPG ===")
    while True:
        print("1. Register\n2. Login\n3. Exit")
        choice = input("Select option: ").strip()
        if choice == '1':
            register_user()
        elif choice == '2':
            username = login_user()
            if username:
                run_game(username)
                break
        elif choice == '3':
            break

if __name__ == '__main__':
    main()
