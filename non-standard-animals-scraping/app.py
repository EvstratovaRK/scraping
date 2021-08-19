import json
from flask import Flask,render_template,jsonify

app = Flask(__name__)

def show_data():
    with open('data.json','r') as file:
        data = json.load(file)
    response = data
    return response


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/data')
def data():
    data = json.dumps(show_data(), ensure_ascii= False, indent=3)
    return render_template('non-standard-animals.html', data=data)

if __name__ == '__main__':
    app.run()