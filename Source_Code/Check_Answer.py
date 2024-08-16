# This is the scope for check answer.
import os


def clear_console():
    os.system('clear')


def check_answer(questions_key, answer_input):
    if questions_key == answer_input:
        print("Correct Answer !!!\n")
    else:
        print("Wrong Answer !!!\n")
    clear_console()