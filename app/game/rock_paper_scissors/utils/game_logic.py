import random

rps_dict = {1: "Rock", 2: "Paper", 3: "Scissors"}
game_state_dict = {1: "win", 2: "tie", 3: "lose"}
results_dict = { 
    "Rock": 
        { 
            "Rock": 2,
            "Paper": 3,
            "Scissors": 1 
        },
    "Paper": 
        { 
            "Rock": 1,
            "Paper": 2,
            "Scissors": 3 
        },
    "Scissors": 
        { 
            "Rock": 3,
            "Paper": 1, 
            "Scissors": 2 
        } 
}

def get_players_choice_value(players_choice_int):
    return rps_dict[players_choice_int]

def get_bots_choice_value():
    #get the bot's choice by taking random number between 1-3
    bots_choice = random.randint(1,3)
    print(f"Bot's choice: {bots_choice}")
    return rps_dict[bots_choice]


def rock_paper_scissors(players_choice_int):
    #get the player and bot's choice values by taking it in rps_dict
    players_choice_value = get_players_choice_value(players_choice_int)
    bots_choice_value = get_bots_choice_value()
    print(f"players_choice_value: {players_choice_value}")
    print(f"bots_choice_value: {bots_choice_value}")

    #check the result
    results = results_dict[players_choice_value][bots_choice_value]

    #bot now checks the result in game_state_dict
    game_state = game_state_dict[results]

    print(f"Player chooses {players_choice_value}!")
    print(f"Bot chooses {bots_choice_value}!")
    print(f"Player {game_state}s against Bot!")

    return game_state