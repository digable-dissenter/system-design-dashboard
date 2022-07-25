from main import app
from flask import request, render_template
from flask_cors import CORS

CORS(app, resources={r"/*":{'origins':"*"}})

@app.route('/', methods=['GET'])
@app.route('/home')
def home_page():
    return("Shark🦈!")

@app.route('/static-reports', methods=['GET'])
def shark():
    return("Shark🦈!")