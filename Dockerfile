# This is a Dockerfile used to build the Image which it'll be used to create a Containers.
FROM ubuntu:latest
LABEL authors="Nicola Ricciardi"
ENTRYPOINT ["top", "-b"]