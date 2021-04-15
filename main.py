from player import Player
from adadachi import Adadachi
from constants import *
import random

player = Player()

def display(statement):
    print(statement)


def create_adadachi():
    print(PET)
    name = input(GET_NAME + "\n")
    foods = player.inventory["foods"]
    games = player.inventory["games"]
    # personality = {
    #     "fav_food": random.randint(0,len(foods)),
    #     "fav_game": random.randint(0,len(games)),
    #     "hates_food": random.randint(0,len(foods)),
    #     "hates_game": random.randint(0,len(games)),
    # }
    personality = {}

    fav_food_ind = random.randrange(0,len(foods))
    personality["fav_food"] = fav_food_ind
    fav_game_ind = random.randrange(0,len(games))
    personality["fav_game"] = fav_game_ind

    hates_food_ind = random.randrange(0,len(foods))
    while fav_food_ind == hates_food_ind:
        hates_food_ind = random.randrange(0,len(foods))
    personality["hates_food"] = hates_food_ind

    hates_game_ind = random.randrange(0,len(games))
    while fav_game_ind == hates_game_ind:
        hates_game_ind = random.randrange(0,len(games))
    personality["hates_game"] = hates_game_ind

    player.adadachi = Adadachi(name,personality)


def start_game():
    display(TITLE)
    answer = input(GREETING)
    if answer.lower() != "y":
        return display(EXIT)
    else:
        create_adadachi()
        while player.adadachi.hunger < 5 or player.adadachi.happiness < 5 \
            or player.adadachi.poop_lvl != 0:
            option = input(OPTIONS).lower()
            if option == "s":
                player.get_status()
            elif option == "c":
                if player.adadachi.poop_lvl == 0:
                    print(f"\n{player.adadachi.name} is very CLEAN!")
                else: 
                    player.clean()
            elif option == "f":
                if player.adadachi.hunger == 5:
                    print(f"\n{player.adadachi.name} is very FULL!")
                else:
                    player.feed()
            elif option == "p":
                if player.adadachi.happiness == 5:
                    print(f"\n{player.adadachi.name} is very HAPPY!")
                else:
                    player.play_with_adadachi()
            elif option == "x":
                return display(EXIT)
            else:
                display(LOST)

    player.get_status()
    return display(WON)

start_game()