#py -m venv venv => venv/scripts/activate => 
#set FLASK_APP=app.py or $env:FLASK_APP = "app.py"
#set FLASK_DEBUG=1 or $env:FLASK_DEBUG=1
#flask run

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World!!</h1>'

@app.route('/about/<username>')
def about(username):
    return f'<h1>About! of {username}</h1>'

if __name__ == "__main__":
    app.run()