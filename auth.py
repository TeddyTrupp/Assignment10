import json
from database import get_connection

def register_user():
    print("\n--- REGISTER NEW ACCOUNT ---")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        print("Username already exists! Try logging in.")
        conn.close()
        return None
    
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    
    initial_state = {
        'hp': 100,
        'max_hp': 100,
        'level': 1,
        'xp': 0,
        'gold': 50,
        'inventory': ['Health Potion'],
        'skills': ['Basic Attack', 'Fireball', 'Heal'],
        'current_map': 'town',
        'quest_progress': {
            'main_quest': 0,
            'side_quest_1': False,
            'side_quest_2': False
        }
    }
    
    cursor.execute('''
        INSERT INTO game_state (username, hp, max_hp, level, xp, gold, inventory, skills, current_map, quest_progress)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        username,
        initial_state['hp'],
        initial_state['max_hp'],
        initial_state['level'],
        initial_state['xp'],
        initial_state['gold'],
        json.dumps(initial_state['inventory']),
        json.dumps(initial_state['skills']),
        initial_state['current_map'],
        json.dumps(initial_state['quest_progress'])
    ))
    
    conn.commit()
    conn.close()
    print("Registration successful! You can now log in.")
    return username

def login_user():
    print("\n--- LOGIN ---")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        print(f"Welcome back, {username}!")
        return username
    else:
        print("Invalid username or password.")
        return None