from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from random import randint
from app.financas.main import bp


@bp.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)

@bp.route('/', defaults={'path': ''})
@bp.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")
