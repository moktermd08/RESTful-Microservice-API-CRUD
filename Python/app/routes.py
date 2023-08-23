from flask import jsonify, request

def configure_routes(app):

    users = {}  # In-memory storage for demonstration

    @app.route('/', methods=['GET'])
    def home():
        return jsonify({"message": "Welcome to the Users API"}), 200

    @app.route('/users', methods=['POST'])
    def create_user():
        user_data = request.json
        if 'id' not in user_data or 'name' not in user_data:
            return jsonify({"message": "Missing id or name"}), 400
        user_id = user_data['id']
        user_name = user_data['name']
        if user_id in users:
            return jsonify({"message": "User ID already exists"}), 400
        users[user_id] = user_name
        return jsonify({"message": "User created successfully"}), 201

    @app.route('/users/<user_id>', methods=['GET'])
    def read_user(user_id):
        user = users.get(user_id)
        if user:
            return jsonify({"name": user}), 200
        return jsonify({"message": "User not found"}), 404
