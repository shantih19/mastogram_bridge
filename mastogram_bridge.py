#!/bin/python
from flask import Flask, request

app = Flask(__name__)

@app.route('/mastogram_bridge')
def main():
    return 'mastogram_bridge'