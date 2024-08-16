# This is a Dockerfile used to build the Image which it'll be used to create a Containers.

# This imgae is created for the Python application, therefore it pull the Python depentencies for the Imgae.
# This is the latest version for Python depentence.
FROM python:latest

# Some Label for the Docker Image.
LABEL multi.authors="Nicola Ricciardi" multi.version="1.0" multi.description="Image attached use for Python APP with Terminal User Input."

# This is the directory where all the following commands will be executed (COPY, RUN, CMD will be executed in the directory WORKDIR specified)
WORKDIR /Docker_Directory

# This command define to copy all the file located in the current directory (" . ") which the Dockerfile is created
# In this case is in the Project APP Python; and copy all files into the specified directory (in thsi case copy all file in the sub-directory "./Image_DIrectory").
# The copy will be placed in the /Docker_Directory/Image_Directory directory.

# Equivalent command -> COPY Local_Path_Where_Dockerfile_Is_Placed /Docker_Directory/Image_Direcotry
COPY . ./Image_Directory

# This command define to run the "main.py" file located under the sub-directory definetd
CMD ["python","Image_Directory/Source_Code/main.py"]