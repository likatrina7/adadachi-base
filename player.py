from constants import *
from game import Game
import random


class Player:
    def __init__(self):
        self.adadachi = None
        self.inventory = {
            "games": ["left or right", "rock scissors paper", "roll dice"],
            "foods": ["banana cream pie", "carrot sticks", "mashed potatoes", "mac 'n cheese", "tater tots", "chocolate cake", "strawberries", "fried rice"],
        }

    # new methods:
    def get_status(self):
        print(STATUS)
        print(f"Name: {self.adadachi.name}")
        print(f"Hunger: {FULL* self.adadachi.hunger}{HUNGERY * (5 - self.adadachi.hunger)}")
        print(f"Happiness: {HAPPY * self.adadachi.happiness}{BORING * (5 - self.adadachi.happiness)}")
        # print(self.adadachi.personality)
        print(f"Favorite food: {self.inventory['foods'][self.adadachi.personality['fav_food']]}")
        print(f"Favorite game: {self.inventory['games'][self.adadachi.personality['fav_game']]}")
        print(f"Hates food: {self.inventory['foods'][self.adadachi.personality['hates_food']]}")
        print(f"Hates food: {self.inventory['games'][self.adadachi.personality['hates_game']]}")
        if self.adadachi.poop_lvl == 0:
            print(f"Poop level: {self.adadachi.name} is clean!")
        else:
            print(f"Poop level: {POOP * self.adadachi.poop_lvl}")

    def clean(self):
        print(SHOWER)
        print(f"Shower is done!\n{self.adadachi.name} looks nice and smells good!")
        self.adadachi.poop_lvl = 0

    def feed(self):
        print(FOOD)
        feed_food = random.randrange(0,len(self.inventory['foods']))
        print(f"{self.adadachi.name} had {self.inventory['foods'][feed_food]}!")   
        
        if feed_food == self.adadachi.personality['fav_food'] and\
            self.adadachi.happiness < 5:
            self.adadachi.happiness += 1
        elif feed_food == self.adadachi.personality['hates_food'] and\
            self.adadachi.happiness > 0:
                self.adadachi.happiness -= 1 
    
        self.adadachi.hunger += 1   

    def play_with_adadachi(self):
        print(GAME)
        game = Game()  

        play_game = random.randrange(0,len(self.inventory['games'])) 
        
        if play_game == 0:
            game.result = game.left_or_right()
        elif play_game == 1:
            game.result = game.rock_scissors_paper()
        else:
            game.result = game.roll_dice()            

        if game.result:
            if play_game == self.adadachi.personality['fav_game'] and\
                self.adadachi.happiness < 4:
                self.adadachi.happiness += 2
            else: 
                self.adadachi.happiness += 1   
        
        if not game.result:
            if play_game == self.adadachi.personality['hates_game'] and\
                self.adadachi.happiness > 1:
                    self.adadachi.happiness -= 1
