from random import randint

from flask import current_app, jsonify, render_template, request

from app.financas.main import bp


@bp.route('/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)


'''@bp.route('/', defaults={'path': ''})
@bp.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")'''
