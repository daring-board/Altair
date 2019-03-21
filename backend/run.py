from flask import Flask, render_template, jsonify, make_response
from random import *
from flask_cors import CORS 

app = Flask(__name__,
            static_folder = "../dist",
            template_folder = "../dist")
CORS(app)

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
#     return render_template("index.html")

@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    print(" * Flask starting server...")
    app.run(host='0.0.0.0',port=5000)