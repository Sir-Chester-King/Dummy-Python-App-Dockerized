# This is the scope for the new game.
import Check_Answer
import Display_Score
import os


# This function just clear the console interpreter to a fancy view.
def clear_console():
    os.system('clear')


def new_game(questions, possible_answer):
    # Initialize a counter for question numbers
    count_questions = 1

    answer_given = []

    # Iterate over the questions and print them
    for key in questions.keys():
        print(F"Question number {count_questions}: {key}")
        print("Options:")

        # So, question number 1 ---> answer number [question - 1]
        for index in possible_answer[count_questions - 1]:
            print(index)

        count_questions += 1  # Index for loop iterate
        answer_input = input("Enter A, B, C or D: ").upper()

        answer_given.append(answer_input)  # Append the input to check after the answer given with the correct answer
        Check_Answer.check_answer(questions.get(key), answer_input)

    questions_value = questions.values()

    see_score = input("You wanna see the score?\nYes or No?").lower()
    if see_score == "yes":
        Display_Score.display_score(questions_value, answer_given)
