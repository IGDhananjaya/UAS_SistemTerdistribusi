from flask import Flask, request, jsonify
from flask.json import JSONError

app = Flask(__name__)

# Replace with a database or a thread-safe data storage mechanism
users = []

@app.route('/api/users', methods=['POST'])
def add_user():
    try:
        user_data = request.get_json()
        if not user_data:
            raise JSONError("Invalid JSON data")
        users.append(user_data)
        return jsonify({"message": "User added successfully", "user": user_data}), 201
    except JSONError as e:
        return jsonify({"error": "Invalid JSON data"}), 400
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)