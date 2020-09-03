from flask import Flask, request, render_template
import requests
import json
import os
import logging

MODEL_PREDICT_ENDPOINT = 'http://machine_learning:5000/model/predict'

app = Flask(__name__)

port = int(os.environ.get('PORT', 5000))

@app.route('/')
def index():
    #return f'''{os.listdir()}'''
    return render_template('./form.html')

@app.route('/submit', methods=['POST'])
def submit():

    long_text = request.form.get('text')

    json_data = {
        'text': [long_text]
    }

    r = requests.post(url=MODEL_PREDICT_ENDPOINT, json=json_data)

    assert r.status_code == 200
    response = r.json()

    return f'You entered: {response}' #'You entered: {}'.format(request.form['text'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)