from flask import Blueprint, request, jsonify

from application.extensions import db
from application.models import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/auth/register", methods=["POST"])
def register():

    data = request.get_json()

    required_fields = ["name", "email", "password"]

    for field in required_fields:
        value = data.get(field)

        if value is None or str(value).strip() == "":
            return jsonify({
                "message": f"{field} is required."
            }), 400

    existing_user = User.query.filter_by(
        email=data["email"]
    ).first()

    if existing_user:
        return jsonify({
            "message": "Email already exists."
        }), 409

    user = User(
        name=data["name"],
        email=data["email"],
        role="trekker",
        phone=data.get("phone")
    )

    user.set_password(data["password"])

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "Registration successful."
    }), 201

@auth_bp.route("/auth/login", methods=["POST"])
def login():

    data = request.get_json()

    required_fields = ["email", "password"]

    for field in required_fields:
        if not data.get(field):
            return jsonify({
                "message": f"{field} is required."
            }), 400
    
    user = User.query.filter_by(email=data["email"]).first()
    
    if not user:
        return jsonify({
            "message": "Invalid email or password."
        }), 401
    
    if not user.check_password(data["password"]):
        return jsonify({
            "message": "Invalid email or password."
        }), 401
    
    if not user.active:
        return jsonify({
            "message": "Your account has been deactivated. Please contact the administrator."
        }), 403
    
    access_token = create_access_token(
        identity=str(user.id),
        additional_claims={
            "role": user.role
        }
    )
    
    return jsonify({
    "message": "Login successful.",
    "access_token": access_token,
    "role": user.role,
    "user": user.name}), 200

@auth_bp.route("/auth/profile", methods=["GET"])
@jwt_required()
def profile():

    user_id = get_jwt_identity()

    user = db.session.get(User, int(user_id))

    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "role": user.role
    })