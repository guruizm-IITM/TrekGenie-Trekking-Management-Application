from flask import Blueprint, request, jsonify

from flask_jwt_extended import jwt_required

from application.extensions import db, cache
from application.models import User
from application.auth_utils import role_required
from application.models import Trek
from datetime import datetime
from application.models import Booking
from sqlalchemy import func, or_


admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin/staff", methods=["POST"])
@jwt_required()
@role_required("admin")
def create_staff():

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

    staff = User(
        name=data["name"],
        email=data["email"],
        role="staff",
        phone=data.get("phone")
    )

    staff.set_password(data["password"])

    db.session.add(staff)
    db.session.commit()

    return jsonify({
        "message": "Staff created successfully."
    }), 201

@admin_bp.route("/admin/staff", methods=["GET"])
@jwt_required()
@role_required("admin")
def get_staff():

    staff_members = User.query.filter_by(role="staff").all()

    result = []

    for staff in staff_members:
        result.append({
            "id": staff.id,
            "name": staff.name,
            "email": staff.email,
            "phone": staff.phone,
            "active": staff.active
        })

    return jsonify(result), 200

@admin_bp.route("/admin/staff/<int:staff_id>/status", methods=["PATCH"])
@jwt_required()
@role_required("admin")
def update_staff_status(staff_id):

    data = request.get_json()

    if "active" not in data:
        return jsonify({
            "message": "active field is required."
        }), 400

    staff = User.query.filter_by(
        id=staff_id,
        role="staff"
    ).first()

    if not staff:
        return jsonify({
            "message": "Staff member not found."
        }), 404

    staff.active = data["active"]

    db.session.commit()

    return jsonify({
        "message": "Staff status updated successfully."
    }), 200



@admin_bp.route("/admin/users/<int:user_id>/status", methods=["PATCH"])
@jwt_required()
@role_required("admin")
def update_user_status(user_id):

    data = request.get_json()

    if "active" not in data:

        return jsonify({
            "message": "active field is required."
        }), 400

    user = User.query.filter_by(
        id=user_id,
        role="trekker"
    ).first()

    if not user:

        return jsonify({
            "message": "User not found."
        }), 404

    user.active = data["active"]

    db.session.commit()

    return jsonify({
        "message": "User status updated successfully."
    }), 200


@admin_bp.route("/admin/treks", methods=["POST"])
@jwt_required()
@role_required("admin")
def create_trek():

    data = request.get_json()

    required_fields = [
        "name",
        "location",
        "difficulty",
        "duration",
        "available_slots",
        "start_date",
        "end_date"
    ]

    for field in required_fields:

        value = data.get(field)

        if value is None or str(value).strip() == "":
            return jsonify({
                "message": f"{field} is required."
            }), 400
        
    allowed_difficulties = ["Easy", "Moderate", "Hard"]

    if data["difficulty"] not in allowed_difficulties:
        return jsonify({
            "message": "Difficulty must be Easy, Moderate or Hard."
        }), 400

    trek = Trek(

        name=data["name"],

        location=data["location"],

        description=data.get("description"),

        difficulty=data["difficulty"],

        duration=data["duration"],

        available_slots=data["available_slots"],

        start_date=datetime.strptime(
            data["start_date"],
            "%Y-%m-%d"
        ).date(),

        end_date=datetime.strptime(
            data["end_date"],
            "%Y-%m-%d"
        ).date()
    )

    db.session.add(trek)

    db.session.commit()
    
    cache.clear()

    return jsonify({
        "message": "Trek created successfully."
    }), 201

@admin_bp.route("/admin/treks", methods=["GET"])
@jwt_required()
@role_required("admin")
def get_treks():

    treks = Trek.query.all()

    result = []

    for trek in treks:

        result.append({

            "id": trek.id,

            "name": trek.name,

            "location": trek.location,

            "difficulty": trek.difficulty,

            "duration": trek.duration,

            "available_slots": trek.available_slots,

            "status": trek.status,

            "assigned_staff_id": trek.assigned_staff_id,

            "start_date": trek.start_date,

            "end_date": trek.end_date,

            "assigned_staff": (
                trek.assigned_staff.name
                if trek.assigned_staff
                else "Not Assigned"
            )

        })

    return jsonify(result), 200


@admin_bp.route("/admin/treks/<int:trek_id>", methods=["GET"])
@jwt_required()
@role_required("admin")
def get_trek(trek_id):

    trek = Trek.query.get(trek_id)

    if not trek:

        return jsonify({
            "message": "Trek not found."
        }), 404

    return jsonify({

        "id": trek.id,

        "name": trek.name,

        "location": trek.location,

        "description": trek.description,

        "difficulty": trek.difficulty,

        "duration": trek.duration,

        "available_slots": trek.available_slots,

        "status": trek.status,

        "assigned_staff_id": trek.assigned_staff_id,

        "start_date": trek.start_date,

        "end_date": trek.end_date,
        

    }), 200

@admin_bp.route("/admin/treks/<int:trek_id>", methods=["PUT"])
@jwt_required()
@role_required("admin")
def update_trek(trek_id):

    trek = Trek.query.get(trek_id)

    if not trek:

        return jsonify({
            "message": "Trek not found."
        }), 404

    data = request.get_json()

    trek.name = data.get("name", trek.name)

    trek.location = data.get("location", trek.location)

    trek.description = data.get("description", trek.description)

    trek.difficulty = data.get("difficulty", trek.difficulty)

    trek.duration = data.get("duration", trek.duration)

    trek.available_slots = data.get(
        "available_slots",
        trek.available_slots
    )

    trek.status = data.get("status", trek.status)

    if data.get("start_date"):

        trek.start_date = datetime.strptime(
            data["start_date"],
            "%Y-%m-%d"
        ).date()

    if data.get("end_date"):

        trek.end_date = datetime.strptime(
            data["end_date"],
            "%Y-%m-%d"
        ).date()

    db.session.commit()
    cache.clear()

    return jsonify({
        "message": "Trek updated successfully."
    }), 200


@admin_bp.route("/admin/treks/<int:trek_id>", methods=["DELETE"])
@jwt_required()
@role_required("admin")
def delete_trek(trek_id):

    trek = db.session.get(Trek, trek_id)

    if not trek:
        return jsonify({
            "message": "Trek not found."
        }), 404

    db.session.delete(trek)
    db.session.commit()

    return jsonify({
        "message": "Trek deleted successfully."
    }), 200

@admin_bp.route("/admin/treks/<int:trek_id>/assign", methods=["PATCH"])
@jwt_required()
@role_required("admin")
def assign_staff(trek_id):

    data = request.get_json()

    if "staff_id" not in data:
        return jsonify({
            "message": "staff_id is required."
        }), 400

    trek = db.session.get(Trek, trek_id)

    if not trek:
        return jsonify({
            "message": "Trek not found."
        }), 404

    staff = User.query.filter_by(
        id=data["staff_id"],
        role="staff",
        active=True
    ).first()

    if not staff:
        return jsonify({
            "message": "Staff member not found or inactive."
        }), 404

    trek.assigned_staff_id = staff.id

    db.session.commit()

    return jsonify({
        "message": "Staff assigned successfully."
    }), 200

@admin_bp.route("/admin/dashboard", methods=["GET"])
@jwt_required()
@role_required("admin")
def admin_dashboard():

    total_users = User.query.filter_by(role="trekker").count()

    total_staff = User.query.filter_by(role="staff").count()

    total_treks = Trek.query.count()

    total_bookings = Booking.query.count()

    active_treks = Trek.query.filter_by(status="Open").count()

    return jsonify({

        "total_users": total_users,

        "total_staff": total_staff,

        "total_treks": total_treks,

        "active_treks": active_treks,

        "total_bookings": total_bookings

    }), 200

@admin_bp.route("/admin/users", methods=["GET"])
@jwt_required()
@role_required("admin")
def get_users():

    users = User.query.filter_by(role="trekker").all()

    result = []

    for user in users:

        result.append({

            "id": user.id,

            "name": user.name,

            "email": user.email,

            "phone": user.phone,

            "active": user.active

        })

    return jsonify(result), 200


@admin_bp.route("/admin/search", methods=["GET"])
@jwt_required()
@role_required("admin")
def search():

    query = request.args.get("q")

    if not query:

        return jsonify({
            "message": "Search query is required."
        }), 400

    users = User.query.filter(

        or_(

            User.name.ilike(f"%{query}%"),

            User.email.ilike(f"%{query}%")

        )

    ).all()

    treks = Trek.query.filter(

        Trek.name.ilike(f"%{query}%")

    ).all()

    return jsonify({

        "users": [

            {

                "id": user.id,

                "name": user.name,

                "role": user.role

            }

            for user in users

        ],

        "treks": [

            {

                "id": trek.id,

                "name": trek.name,

                "location": trek.location

            }

            for trek in treks

        ]

    }), 200

@admin_bp.route("/admin/bookings", methods=["GET"])
@jwt_required()
@role_required("admin")
def get_bookings():

    bookings = Booking.query.all()

    result = []

    for booking in bookings:

        result.append({

            "booking_id": booking.id,

            "trekker": booking.user.name,

            "trek": booking.trek.name,

            "booking_status": booking.booking_status,

            "payment_status": booking.payment_status,

            "booking_date": booking.booking_date

        })

    return jsonify(result), 200