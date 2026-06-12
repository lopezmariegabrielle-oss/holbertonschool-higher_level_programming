from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    return jsonify(list(users.keys()))


@app.route('/status')
def check_status():
    return "OK"


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    users[username] = data
    return jsonify({"message": "User added successfully"}), 201


if __name__ == '__main__':
    app.run()
