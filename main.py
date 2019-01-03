from flask import Flask, render_template, jsonify

app = Flask(__name__, static_folder = "./dist/static", template_folder = "./dist")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello_world():
    return "Hello World!", 200

app.run()