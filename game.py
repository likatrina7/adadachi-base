import random

class Game:
    def __init__(self):
        self.result = None

    def left_or_right(self):
        player_guess = input("let's play left or right! Please make a guess: \n\n").lower()
        direction = random.choice(("left", "right"))

        if direction == player_guess.lower():
            print(f"\nYour guess {player_guess.upper()} is correct, you won the game!")
            return True  
        else:
            print(f"\nYour guess {player_guess.upper()} is wrong, you lose the game!")
            return False

    def rock_scissors_paper(self):
        player_input = input("let's play rock scissors paper!\n\nEnter rock/scissors/paper:\n\n").lower()
        random_rsp = random.choice(("rock", "scissors", "paper"))

        if player_input == random_rsp:
            print("It's a tie!")
        elif player_input == "scissors":
            if random_rsp == "rock":
                print (f"\nYour opponent played {random_rsp}, you lose the game!")
                return False
            else:
                print (f"\nYour opponent played {random_rsp}, you won the game!")
                return True
        elif player_input == "rock":
            if random_rsp == "scissors":
                print (f"\nYour opponent played {random_rsp}, you won the game!")
                return True
            else:
                print (f"\nYour opponent played {random_rsp}, you lose the game!")
                return False
        elif player_input == "paper":
            if random_rsp == "scissors":
                print (f"\nYour opponent played {random_rsp}, you lose the game!")
                return False
            else:
                print (f"\nYour opponent played {random_rsp}, you won the game!")
                return True

    def roll_dice(self):
        print("let's play roll dice! If you get 6 you win!\n\n\t Rolling dice....\n")
        num = random.randint(1, 6)

        if num == 6:
            print(f"Your got 6, you won the game!")
            return True  
        else:
            print(f"Your got {num}, you lose the game!")
            return False
