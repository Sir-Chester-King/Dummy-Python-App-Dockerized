# This is the scope for the display the score.
import os


# This function just clear the console interpreter to a fancy view.
def clear_console():
    os.system('clear')


def display_score(questions_value, answer_given):
    clear_console()
    correct_answer = 0
    list_question_value = []

    # Convert a dictionary to a Tuple list
    for value in questions_value:
        list_question_value.append(value)

    print("Answer given: ", end="")
    for index in answer_given:
        print(index, end="")

    print("\n")
    print("Correct answer: ", end="")
    for index in list_question_value:
        print(index, end="")

    for index in range(0, len(answer_given)):
        if list_question_value[index] == answer_given[index]:
            correct_answer += 1
    score = (correct_answer / len(questions_value)) * 100

    print("\n")
    print("Score: ", score)
