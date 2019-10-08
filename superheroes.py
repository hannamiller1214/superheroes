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
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.ability = self.abilities.append(ability)

    def attack(self):
        total_strength = 0
        for ability in self.abilities:
            total_strength = total_strength + ability.attack()
        return total_strength

    def add_armor(self, armor):
        self.armor = self.armors.append(armor)

    def defend(self, damage_amt):
        total_damage = 0
        if self.current_health > 0:
            for armor in self.armors:
                total_damage = damage_amt - armor.block()
        return total_damage

    def take_damage(self, damage):
        if self.current_health <= 0:
            self.deaths += 1
        elif self.current_health <= damage:
            self.current_health -= damage
            self.deaths += 1
        else:
            self.current_health -= damage

    def is_hero_alive(self):
        return self.current_health > 0

    def add_kill(self, num_kills):
        self.num_kills += self.kills

    def add_deaths(self, num_deaths):
        self.num_deaths += self.deaths

    def fight(self, opponent):
        print("Fight Start!")
        while self.is_hero_alive() == True and opponent.is_hero_alive() == True:
            print(self.name, "is attacking", opponent.name)
            self.take_damage(opponent.attack())
            print(opponent.name, "is attacking", self.name)
            opponent.take_damage(self.attack())
        if self.is_hero_alive() == False:
            print(self.name, "has died")
            print(opponent.name, "wins!")
            self.deaths += 1
            opponent.kills += 1
        elif opponent.is_hero_alive() == False:
            print(opponent.name, "has died")
            print(self.name, "wins!")
            opponent.deaths += 1
            self.kills += 1

    def add_weapon(self, weapon):
        self.weapon = self.abilities.append(weapon)

class Weapon(Ability):
    def attack(self):
        self.half_attack = self.max_damage
        weapon_strength = random.randint(0, self.half_attack)
        return weapon_strength

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                hero_num = self.heroes.index(hero)
                self.heroes.pop(hero_num)
            else:
                return 0

    def add_hero(self, hero):
        self.hero = self.heroes.append(hero)

    def view_all_heroes(self):
        if len(self.heroes) == 0:
            print("There are no heroes")
        else:
            for hero in self.heroes:
                print(hero.name)

    # def attack(self, other_team):

    def is_team_alive(self):
        is_team_alive = []
        for hero in self.heroes:
            if hero.is_hero_alive():
                is_team_alive.append(hero)
        return is_team_alive

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = health
            return hero.current_health

    def stats(self):
        for hero in self.heroes:
            print(hero.name, "has defeated", str(hero.kills), "opponents and has been defeated", str(hero.deaths), "times")

class Arena:
    def __init__(self):
        self.team_one = []
        self.team_two = []

    def create_ability(self):
        ability_name = input("Name the new ability for your hero! > ")
        ability_strength = int(input("How strong would you like this ability to be? > "))
        new_ability = Ability(ability_name, ability_strength)
        return new_ability

    def create_weapon(self):
        weapon_name = input("Name the new weapon for your hero! > ")
        weapon_strength = int(input("How strong would you like this weapon to be? > "))
        new_weapon = Weapon(weapon_name, weapon_strength)
        return new_weapon

    def create_armor(self):
        armor_name = input("Name the new armor for your hero! > ")
        armor_strength = int(input("How strong would you like this armor to be? > "))
        new_armor = Armor(armor_name, armor_strength)
        return new_armor

    def create_hero(self):
        hero_name = input("Name your hero! > ")
        new_hero = Hero(hero_name)
        new_hero.add_ability(self.create_ability())
        new_hero.add_weapon(self.create_weapon())
        new_hero.add_armor(self.create_armor())
        return new_hero

    def build_team_one(self):
        team_one_name = input("Let's give your first team a name! > ")
        self.team_one = Team(team_one_name)
        heroes_in_team_one = int(input("How many heroes are in " + team_one_name + "? > "))
        while heroes_in_team_one > 0:
            new_hero = self.create_hero()
            heroes_in_team_one -= 1
            self.team_one.add_hero(new_hero)
        return self.team_one

    def build_team_two(self):
        team_two_name = input("Let's give your second team a name! > ")
        self.team_two = Team(team_two_name)
        heroes_in_team_two = int(input("How many heroes are in " + team_two_name + "? > "))
        while heroes_in_team_two > 0:
            new_hero = self.create_hero()
            heroes_in_team_two -= 1
            self.team_two.add_hero(new_hero)
        return self.team_two

    def team_battle(self):
        print("Team Battle Start!")
        while self.team_one.is_team_alive() == True and self.team_two.is_team_alive() == True:
            self.team_one.attack(self.team_two)
            self.team_two.attack(self.team_one)
        # Look into replacing "Team One" and "Team Two" with the names you entered
        if len(self.team_one.heroes) <= 0:
            print("Team One Wins!")
        else:
            print("Team Two Wins!")
# Stats are not updating correctly
    def show_stats(self):
        print("Team One's Stats > ")
        self.team_one.stats()
        print("Team Two's Stats > ")
        self.team_two.stats()

if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()

# if __name__ == "__main__":
#     game_is_running = True
#     arena = Arena()
#
#     arena.build_team_one()
#     arena.build_team_two()
#
#     while game_is_running:
#         arena.team_battle()
#         arena.show_stats()
#         play_again = input("Play Again? Y or N >")
#
#         if play_again.lower() == "n":
#             game_is_running = False
#         else:
#             arena.team_one.revive_heroes()
#             arena.team_two.revive_heroes()
