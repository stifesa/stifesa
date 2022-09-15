# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import numpy as np
from flask import Flask, request, jsonify, render_template

import pickle

app = Flask(__name__)


@app.route("/")
def home():
    return "hola mundo"


app.run()
