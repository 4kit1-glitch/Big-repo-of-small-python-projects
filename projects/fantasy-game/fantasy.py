# a simple fantasy game

from typing import Any
class Human:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    




class Org:
    pass
class Elf:
    pass
class Player:
    DEFAULT_INVENTORY={"gold": 0, "weapon": None }

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.inventory = self.DEFAULT_INVENTORY.copy()
        self.weapon = self.inventory["weapon"]

    def fight(self):
        if self.weapon == None:
            print("Find a weapon to fight")
        print(f"ahh attacks with {self.weapon}")

    def collect(self, value: Any):
        print(f"collected {value}")
        self.inventory[value] = value

    def move_forward(self):
        print("shshs.. moves forward")
    def move_backward(self):
        print("shshs.. moves back")
    def move_left(self):
        print("shshs.. moves right")
    def move_right(self):
        print("shshs.. moves left")
    pass


def battle(hero: Player, enemy: Any):
    pass

def create_user():
    pass
def play_game():
    pass

def end_game():
    pass

def main():
    pass