# This is the main scope about this project
import os
import New_Game
import Play_Again


# This function just clear the console interpreter to a fancy view.
def clear_console():
    os.system('clear')


clear_console()
print("Hello gamer, here a simple Quiz game thought to entertainment you.\n\nEnjoy it!!!\n")

questions = {
    "Who is the first American's President?": "B",
    "When was the second world war?": "A",
    "In which country was invented the pizza?": "C"
}

answer = [
    ["A. Joe Biden", "B. George Washington", "C. Barack Obama", "D. John Kennedy"],
    ["A. 1940", "B. 2001", "C. 1390", "D. 1930"],
    ["A. France", "B. United Kingdom", "C. Italy", "D. America"]
]

New_Game.new_game(questions, answer)

new_game = input("You wanna play again?\nYes or No?").lower()
while new_game == "yes":
    Play_Again.play_again(questions, answer)
    new_game = input("You wanna play again?\nYes or No?").lower()


print("Goodbye !!!")
