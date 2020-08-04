IMAGE_NAME=python:3.6-slim

docker run -it --rm \
           -v $PWD:/home \
           ${IMAGE_NAME} /bin/bash
