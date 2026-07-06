from flask import Blueprint, jsonify, request

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from application.extensions import db
from application.models import User, Trek
from application.auth_utils import role_required

staff_bp = Blueprint("staff", __name__)

@staff_bp.route("/staff/dashboard", methods=["GET"])
@jwt_required()
@role_required("staff")
def dashboard():

    staff_id = int(get_jwt_identity())

    assigned_treks = Trek.query.filter_by(
        assigned_staff_id=staff_id
    ).count()

    active_treks = Trek.query.filter_by(
        assigned_staff_id=staff_id,
        status="Open"
    ).count()

    completed_treks = Trek.query.filter_by(
        assigned_staff_id=staff_id,
        status="Completed"
    ).count()

    return jsonify({

        "assigned_treks": assigned_treks,

        "active_treks": active_treks,

        "completed_treks": completed_treks

    }), 200

@staff_bp.route("/staff/treks", methods=["GET"])
@jwt_required()
@role_required("staff")
def my_treks():

    staff_id = int(get_jwt_identity())

    treks = Trek.query.filter_by(
        assigned_staff_id=staff_id
    ).all()

    result = []

    for trek in treks:

        result.append({

            "id": trek.id,

            "name": trek.name,

            "location": trek.location,

            "difficulty": trek.difficulty,

            "status": trek.status,

            "available_slots": trek.available_slots

        })

    return jsonify(result), 200


@staff_bp.route("/staff/treks/<int:trek_id>/status", methods=["PATCH"])
@jwt_required()
@role_required("staff")
def update_trek_status(trek_id):

    staff_id = int(get_jwt_identity())

    trek = Trek.query.filter_by(
        id=trek_id,
        assigned_staff_id=staff_id
    ).first()

    if not trek:
        return jsonify({
            "message": "Trek not found."
        }), 404

    data = request.get_json()

    if "status" not in data:
        return jsonify({
            "message": "status is required."
        }), 400

    allowed_status = [
        "Open",
        "Closed",
        "Completed"
    ]

    if data["status"] not in allowed_status:
        return jsonify({
            "message": "Invalid status."
        }), 400

    trek.status = data["status"]

    db.session.commit()

    return jsonify({
        "message": "Status updated successfully."
    }), 200

@staff_bp.route("/staff/treks/<int:trek_id>/slots", methods=["PATCH"])
@jwt_required()
@role_required("staff")
def update_slots(trek_id):

    staff_id = int(get_jwt_identity())

    trek = Trek.query.filter_by(
        id=trek_id,
        assigned_staff_id=staff_id
    ).first()

    if not trek:
        return jsonify({
            "message": "Trek not found."
        }), 404

    data = request.get_json()

    if "available_slots" not in data:
        return jsonify({
            "message": "available_slots is required."
        }), 400

    trek.available_slots = data["available_slots"]

    db.session.commit()

    return jsonify({
        "message": "Available slots updated successfully."
    }), 200

@staff_bp.route("/staff/treks/<int:trek_id>/participants", methods=["GET"])
@jwt_required()
@role_required("staff")
def view_participants(trek_id):

    staff_id = int(get_jwt_identity())

    trek = Trek.query.filter_by(
        id=trek_id,
        assigned_staff_id=staff_id
    ).first()

    if not trek:
        return jsonify({
            "message": "Trek not found."
        }), 404

    result = []

    for booking in trek.bookings:

        result.append({

            "booking_id": booking.id,

            "name": booking.user.name,

            "email": booking.user.email,

            "booking_status": booking.booking_status,

            "payment_status": booking.payment_status

        })

    return jsonify(result), 200