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

@app.route('/market')
def market_page():
    items = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
]
    return render_template('market.html', items=items)

if __name__ == "__main__":
    app.run(debug=True)