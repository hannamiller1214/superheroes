import random

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        attack_value = random.randint(0, self.max_damage)
        return attack_value

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        block_strength = random.randint(0, self.max_block)
        return block_strength

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = 100
        self.current_health = starting_health

    def add_ability(self, ability):
        self.ability = self.abilities.append(ability)

    def attack(self):
        total_strength = 
        for ability in self.abilities:
            Ability.attack()
        return total_strength

    def add_armor(self, armor):
        self.armor = self.armors.append(armor)

    # def defend(self, damage_amt):
    #     self.damage_amt =
    #     for defend in self.armors:


if __name__ == "__main__":
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())
