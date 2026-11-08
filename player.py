import json
from database import get_connection

class Player:
    def __init__(self, username):
        self.username = username
        self.load_data()

    def load_data(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT hp, max_hp, level, xp, gold, inventory, skills, current_map, quest_progress FROM game_state WHERE username = ?", (self.username,))
        data = cursor.fetchone()
        conn.close()
        
        if data:
            self.hp = data[0]
            self.max_hp = data[1]
            self.level = data[2]
            self.xp = data[3]
            self.gold = data[4]
            self.inventory = json.loads(data[5])
            self.skills = json.loads(data[6])
            self.current_map = data[7]
            self.quest_progress = json.loads(data[8])

    def save_data(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE game_state 
            SET hp = ?, max_hp = ?, level = ?, xp = ?, gold = ?, inventory = ?, skills = ?, current_map = ?, quest_progress = ?
            WHERE username = ?
        ''', (
            self.hp,
            self.max_hp,
            self.level,
            self.xp,
            self.gold,
            json.dumps(self.inventory),
            json.dumps(self.skills),
            self.current_map,
            json.dumps(self.quest_progress),
            self.username
        ))
        conn.commit()
        conn.close()

    def view_status(self):
        print(f"\n=== PLAYER STATUS: {self.username} ===")
        print(f"Level: {self.level} | XP: {self.xp}")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"Gold: {self.gold} coins")
        print(f"Skills: {', '.join(self.skills)}")
        print(f"Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")
        print(f"Current Location: {self.current_map}")