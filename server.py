#!/usr/bin/env python3

from flask import Flask, jsonify
from fundamentus import get_data
from datetime import datetime
import os

# ON_HEROKU = os.environ.get('ON_HEROKU')
# if ON_HEROKU:
    # get the heroku port
PORT = int(os.environ.get('PORT'))  # as per OP comments default is 17995
# else:
    # PORT = 3000

app = Flask(__name__)

# First update
lista, dia = dict(get_data()), datetime.strftime(datetime.today(), '%d')
lista = {outer_k: {inner_k: float(inner_v) for inner_k, inner_v in outer_v.items()} for outer_k, outer_v in lista.items()}

@app.route("/")
def json_api():
    global lista, dia
    
    # Then only update once a day
    if dia == datetime.strftime(datetime.today(), '%d'):
        return jsonify(lista)
    else:
        lista, dia = dict(get_data()), datetime.strftime(datetime.today(), '%d')
        lista = {outer_k: {inner_k: float(inner_v) for inner_k, inner_v in outer_v.items()} for outer_k, outer_v in lista.items()}
        return jsonify(lista)

app.run(port=PORT)
