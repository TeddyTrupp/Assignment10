class Monster:
    def __init__(self, name, hp, attack, xp_reward, gold_reward):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.xp_reward = xp_reward
        self.gold_reward = gold_reward

class Goblin(Monster):
    def __init__(self):
        super().__init__("Goblin", 40, 8, 20, 15)

class Orc(Monster):
    def __init__(self):
        super().__init__("Orc", 60, 12, 35, 25)

class Skeleton(Monster):
    def __init__(self):
        super().__init__("Skeleton", 50, 10, 30, 20)

class Wolf(Monster):
    def __init__(self):
        super().__init__("Wild Wolf", 35, 9, 15, 10)

class Boss(Monster):
    def __init__(self):
        super().__init__("Dark Overlord (Boss)", 150, 25, 200, 100)
