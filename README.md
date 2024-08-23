# Python Application Using <ins>**Docker Technology**</ins>
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

<a name="display_score.py"></a>
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
This file contain all commands used to build the Image that Containers will use.<br>
The Image is a snapshot of the source code, and when it did build, the Image is in read-only mode, and you cannot change the code. If you want to create a container based to the new image, you must re-build the image.

<a name="command"></a>
### Command Image
The commands used to build the image that it'll be used to create the container that has the code, you must declare some parameters.<br>
In this image it used the following commands:
- FROM
- LABEL
- WORKDIR
- COPY
- CMD

The <strong> FROM </strong> command it used to pull all dependenties based on the image that we pass as a parameter.<br>
In this case, we defined an image for a Python appl, therefore with this command, we pull oll the dependenties from the <ins>official</ins> Python Imgae, stored in the [Docker Hub](https://hub.docker.com).
```
FROM python:latest
```
The word "<b> latest </b>" define to use the latest versione of the image we want to pull.<br><br>

The <strong> WORKDIR </strong> command it used to define our work directory that all the <mark> next following command in the Dockerfile </strong> will be executed.<br>
```
# This is the directory where all the following commands will be executed (COPY, RUN, CMD will be executed in the directory WORKDIR specified)
WORKDIR /Docker_Directory
```


The <strong> COPY </strong> command it used to say to Docker, that it must copy all the file stored in the same directory of Dockerfile, to some directory in the container (that we pecified)
```
# This command define to copy all the file located in the current directory (" . ") which in the Dockerfile is created
# In this case is in the Project APP Python; and copy all files into the specified directory (copy all file in the sub-directory "./Image_DIrectory").
# The copy will be placed in the /Docker_Directory/Image_Directory directory.

# Equivalent command -> COPY Local_Path_Where_Dockerfile_Is_Placed /Docker_Directory/Image_Direcotry
COPY . ./Image_Directory
```

The <strong> CMD </strong> command it used to say to Docker to run the command we specified in the dockerfile.
```
# This command define to run the "main.py" file located under the sub-directory definetd
CMD ["python","Image_Directory/Source_Code/main.py"]
```
<a name="build"></a>
### Build Image
To build image, you must use the <strong> BUILD </strong> command, and pass where the dockerfile is stored, as a parameter.<br>
It be the result.<br>
![Alt text](Readme_Screen/Build%20Command.png)
![Alt text](Readme_Screen/Execute%20Command%20Build.png)
To view the image was builted, you can view with the following command:
```
docker image ls
```
![Alt text](Readme_Screen/List%20Images.png)

<a name="run"></a>
### Run The Container
After you successfully build the Image, you can create and run the Container will contain the python app.<br>
To crate the container, you must use the following command:
```
docker run --name Container_App_Python -it 296ac232d224
```
If you see a stranger string <ins>(296ac232d224)</ins>, it's 'cause, it is the ID of Image builted previously.<br>
When you create the container, the app start immediatly, 'cause, in the Dockerfile we declared a CMD command the run the "main.py" file.<br>
![Alt text](Readme_Screen/App%20Running.png)
If you wanna see the list of container created, you must use the following command:
```
docker ps
```
if you wanna see the list of container that no longer used, for example, such as it was terminated 'cause the app in the container finished the work.<br>
You must use the following command:
```
docker ps -a
```
