from flask import current_app, jsonify, render_template, request
from random import randint
from app.financas.api import api, calculo

@api.route("/incluir", methods = ['GET','POST'])
def incluir():
    return "Funcionou"
