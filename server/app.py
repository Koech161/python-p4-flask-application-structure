#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

@app.route('/<string:abel>')
def user(abel):
    return f'<h1>Profile for {abel}</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
