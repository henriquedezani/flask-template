from flask import Flask
app = Flask(__name__)
# socket_ = SocketIO(app)


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()

# https://realpython.com/flask-by-example-part-1-project-setup/
# $ touch app.py .gitignore README.md requirements.txt
# $ python -m pip install Flask==1.1.1
# $ python -m pip freeze > requirements.txt
# $ python app.py

# https://medium.com/swlh/implement-a-websocket-using-flask-and-socket-io-python-76afa5bbeae1

