class Skill:
    def __init__(self, name, mana_cost, cooldown):
        self.name = name
        self.mana_cost = mana_cost
        self.cooldown = cooldown

    def use(self, caster, target):
        raise NotImplementedError

class Fireball(Skill):
    def __init__(self):
        super().__init__("Fireball", 10, 2)

    def use(self, caster, target):
        damage = 25
        target.hp -= damage
        print(f"{caster.name} casts Fireball on {target.name} for {damage} damage!")

class Heal(Skill):
    def __init__(self):
        super().__init__("Heal", 15, 3)

    def use(self, caster, target):
        heal_amount = 30
        caster.hp = min(caster.max_hp, caster.hp + heal_amount)
        print(f"{caster.name} casts Heal and restores {heal_amount} HP!")
