#docker run --dns 8.8.8.8 -t hello-python
docker run --env-file $1 -p 3000:3000 -t hello-python