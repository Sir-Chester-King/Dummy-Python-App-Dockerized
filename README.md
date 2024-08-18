# Python Application Using <ins>**Docker**</ins> Container
## Table Of Contents
* [Description](#description)
* [Main Application](#main_application)
  - [Main.py](#main.py)
  - [New_Game.py](#new_game.py)
  - [Display_Score.py](#display_score.py)
  - [Check_Answer.py](#check_answer.py)
  - [Play_Again.py](#play_again.py)
* [Dockerfile](#dockerfile)
  - [Command Image](#command)
  - [Build Image](#build)
  - [Run Container](#run)

---
<a name="description"></a> 
## Description
This application is a simple a quiz game, as education purpose to take conscious of how application is used within a container using the [Docker](https://www.docker.com) technology to containeraize the application innit.<br>
The application ask to an user to answer a simple question via terminal command (NO GUI).<br>
The application is write in [Python](https://www.python.org) and use the user input via command terminal to continue the usage.

---
<a name="main_application"></a>
## Main Application
The application ask to an user to answer a simple question via terminal command (NO GUI), and it wrote in [Python](https://www.python.org).<br>
Questions available are:
```
questions = {
    "Who is the first American's President?": "B",
    "When was the second world war?": "A",
    "In which country was invented the pizza?": "C"
}
```
As you can see, it was used a dictionary for the questions to use the pair <ins><em>Key: Values</em></ins> to bind the correct answer with the correct question.

<a name="main.py"></a>
### Main.py
This function is structured with the questions and the correct answers, store in the main body of application.<br>
After that, it call another function called [New_Game.py](#new_game.py)<br>

<a name="new_game.py"></a>
### New_Game.py
Thsi function use a nested <mark>FOR cycle</mark> to iterate first one, the questions dictionary (to show one question per time), and the second one, the answer (to show all possible answer per question).
```
    # Iterate over the questions and print them
    for key in questions.keys():
        print(F"Question number {count_questions}: {key}")
        print("Options:")

        # So, question number 1 ---> answer number [question - 1]
        for index in possible_answer[count_questions - 1]:
            print(index)
```
The variable index "<strong>count_questions</strong>" start from one 'cause it was used to show the number of question showed to user (ex: question number 1°).

<a name="display_score.py></a>
### Display_Score.py
This function show the answer that user choose during the game, and all the correct answer for all the questions.
It shiw the score percentage of result too.
```
print("Answer given: ", end="")
for index in answer_given:
    print(index, end="")

print("\n")
print("Correct answer: ", end="")
for index in list_question_value:
    print(index, end="")
```
```
score = (correct_answer / len(questions_value)) * 100
print("\n")
print("Score: ", score)
```

<a name="check_answer.py"></a>
### Check_Answer.py
This function check only if the answer that user given during the game it was right.
```
def check_answer(questions_key, answer_input):
    if questions_key == answer_input:
        print("Correct Answer !!!\n")
    else:
        print("Wrong Answer !!!\n")
```

<a name="play_again.py"></a>
### Play_Again.py
This function call the [New_Game.py](#new_game.py) when the game reached the end, and the user wants to play again.
```
def play_again(questions, possible_answer):
    New_Game.new_game(questions, possible_answer)
```

---
<a name="dockerfile"></a>
## Dockerfile
This file contain all commands used to build the Image that Containers will use.
The Image is a snapshot of the source code, and when it did build, the Image is in read-only mode, and you cannot change the code.
