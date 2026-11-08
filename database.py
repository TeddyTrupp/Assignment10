import sqlite3

def get_connection():
    return sqlite3.connect('rpg_game.db')

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS game_state (
            username TEXT PRIMARY KEY,
            hp INTEGER,
            max_hp INTEGER,
            level INTEGER,
            xp INTEGER,
            gold INTEGER,
            inventory TEXT,
            skills TEXT,
            current_map TEXT,
            quest_progress TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()
