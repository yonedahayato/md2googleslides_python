IMAGE_NAME=md2gslides

docker build -t ${IMAGE_NAME} .
docker run -it --rm \
           -v $PWD/secrets:/home/secrets \
           --entrypoint "/bin/bash" \
           ${IMAGE_NAME}
docker rmi ${IMAGE_NAME}
