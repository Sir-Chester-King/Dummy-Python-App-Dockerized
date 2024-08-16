# This is a Dockerfile used to build the Image which it'll be used to create a Containers.

# This imgae is created for the Python application, therefore it pull the Python depentencies for the Imgae.
# The versione is the lastes for the major version 3.
FROM python

# Author of the Image.
LABEL multi.authors="Nicola Ricciardi" multi.version="1.0" multi.description="Image attached use for Python APP with Terminal User Input."

WORKDIR /Source_Code

COPY . /Image_Directory

CMD ["python","main.py"]