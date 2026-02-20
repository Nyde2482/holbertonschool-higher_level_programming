#!/usr/bin/python3
"""
Flask API with basic and JWT authentication.

This module provides endpoints for user management, authentication (basic and JWT),
and demonstrates protected routes. It uses Flask, flask_httpauth, and flask_jwt_extended.
"""
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt

auth = HTTPBasicAuth()
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "jesuispasla"
jwt = JWTManager(app)


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing or invalid JWT token errors."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid JWT token errors."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err, ):
    """Handle expired JWT token errors."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handle revoked JWT token errors."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handle errors when a fresh JWT token is required."""
    return jsonify({"error": "Fresh token required"}), 401


user_data = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def verfify_password(username, password):
    """Verify a user's password for HTTP Basic Auth.

    Args:
        username (str): The username provided in the request.
        password (str): The plaintext password provided in the request.

    Returns:
        str or None: The username if credentials are valid, None otherwise.
    """
    if username in user_data and \
            check_password_hash(user_data[username]["password"], password):
        return username


@app.route("/")
def home():
    """Return a welcome message for the API."""
    return "Welcome to the Flask API!", 200


@app.route("/data", methods=["GET"])
def get_all_user():
    """Return a JSON list of all usernames."""
    names = [user["username"] for user in user_data.values()]
    return jsonify(names), 200


@app.route("/status", methods=["GET"])
def status():
    """Return the API status."""
    return "OK", 200


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return data for a specific user by username.

    Args:
        username (str): The username to look up.

    Returns:
        flask.Response: User data if found, or an error message with 404.
    """
    user_info = user_data.get(username)
    if user_info:
        return jsonify(user_info), 200
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Create a new user from a JSON request body.

    Expected JSON keys:
        - username (required)
        - name (optional)
        - age (optional)
        - city (optional)

    Returns:
        flask.Response: Confirmation message and created user data.
    """
    new_user = request.get_json()

    if not new_user:
        return jsonify(error="Invalid JSON"), 400

    if "username" not in new_user:
        return jsonify({"error": "Username is required"}), 400

    if new_user["username"] in user_data:
        return jsonify({"error": "Username already exists"}), 409

    username = new_user["username"]

    user_data[username] = {
        "username": username,
        "name": new_user.get("name", ""),
        "age": new_user.get("age", ""),
        "city": new_user.get("city", "")
    }
    return jsonify(message="User added", user=user_data[username]), 201


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def auth_message():
    """Return a success message for Basic Auth protected route."""
    return "Basic Auth: Access Granted", 200


@app.route("/login", methods=["POST"])
def loginAuth():
    """Authenticate a user and return a JWT access token.

    Expected JSON keys:
        - username (str): The user's username.
        - password (str): The user's plaintext password.

    Returns:
        flask.Response: A JWT access token on success, or an error message.
    """
    user = request.get_json()
    if not "username" in user\
            or not "password" in user:
        return jsonify({"error": "Missing fields"}), 400
    if not user["username"] in user_data:
        return jsonify({"error": "Invalid credentials"}), 401
    pass_hash = user_data[user["username"]]["password"]
    pass_role = user_data[user["username"]]["role"]
    if check_password_hash(pass_hash, user["password"]) is False:
        return jsonify({"error": "Invalide password"}), 401
    else:
        return jsonify({"access_token": create_access_token(identity=user["username"], additional_claims={"role": pass_role})}), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def access_granted():
    """Return a success message for JWT protected route."""
    return ("JWT Auth: Access Granted"), 200


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Return a success message only for users with the admin role.

    Returns:
        flask.Response: Success message if role is admin, or 403 error.
    """
    claims = get_jwt()
    if claims["role"] == "admin":
        return "Admin Access: Granted", 200
    else:
        return jsonify({"error": "Admin access required"}), 403


if __name__ == "__main__":
    app.run()
