docker build -t flask-app-small .

docker run -d -p 5555:5555 -e PORT=5555 flask-app-small
