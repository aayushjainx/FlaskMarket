#py -m venv venv => venv/scripts/activate => 
#set FLASK_APP=app.py or $env:FLASK_APP = "app.py"
#set FLASK_DEBUG=1 or $env:FLASK_DEBUG=1
#flask run

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)