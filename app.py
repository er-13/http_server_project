from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users", methods=["POST"])
def add_user():
    new_user = request.json
    users.append(new_user)
    return jsonify({"message": "User added", "user": new_user}),201

@app.route("/users/<int:user_id>",methods=["PUT"])
def update_user(user_id):
    for user in users:
        if user ["id"] == user_id:
            user.update(request.json)
            return jsonify ({"message": "Users updated", "users": user})
    return jsonify ({"error": "User not found"}), 404

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify ({"message": "User deleted"})

if __name__ == "__main__":
    app.run(debug=True)
