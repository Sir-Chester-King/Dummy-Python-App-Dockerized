# This file is used for the function Play_Again()
import os

import New_Game


# This function just clear the console interpreter to a fancy view.
def clear_console():
    os.system('clear')


def play_again(questions, possible_answer):
    New_Game.new_game(questions, possible_answer)
