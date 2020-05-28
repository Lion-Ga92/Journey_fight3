import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, hp, atk, hep, npotions, max_npotions):
        self.npotions = npotions
        self.maxnpotions = npotions
        self.npotionsl = npotions - 5
        self.npotionsh = npotions - 1
        self.maxhp = hp
        self.hp = hp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.hepl = hep + 5
        self.heph = hep + 10
        self.hep = hep
        self.action = ("fight", "heal", "run")
        self.crAction = ("Fght", "Run")


    def get_hp(self):
        return self.hp

    def full_restore(self):
        if self.hp < 400:
            self.hp = 400

    def generate_hep(self):
        return random.randrange(self.hepl, self.heph)

    def take_heal(self, heal):
        self.hp += heal
        if self.hp < 0:
            return self.hp

    def choose_action(self):
        i = 1
        print("Action")
        for item in self.action:
            print(str(i) + ":" + item)
            i += 1

    def choose_crAction(self):
            i = 1
            print("crAction")
            for item in self.crAction:
                print(str(i) + ":" + item)
                i += 1


    def get_max_hp(self):
        return self.hp

    def generate_damage(self):
            return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
            return self.hp

    def get_npotions(self):
        return self.npotions

    def get_max_npotions(self):
        return self.maxnpotions

    def generate_npotions(self):
        return random.randrange(self.npotionsl, self.npotionsh)

    def add_potions(self, plus_potions):
        self.npotions += plus_potions
        return self.npotions


    def take_potions(self):
        self.npotions -= 1
        if self.npotions < 0:
            self.npotions = 0
            return self.npotions
class Creature:
    def __init__(self, hp, atk):
        self.maxhp = hp
        self.hp = hp
        self.atkl = atk - 10
        self.atkh = atk + 20
        self.crAction = ("Fight", "Run")

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.hp

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
            return self.hp



