from flask import Blueprint, jsonify, request

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from application.extensions import db

from application.models import (
    User,
    Trek,
    Booking
)

from application.auth_utils import role_required

trekker_bp = Blueprint("trekker", __name__)

@trekker_bp.route("/trekker/dashboard", methods=["GET"])
@jwt_required()
@role_required("trekker")
def dashboard():

    user_id = int(get_jwt_identity())

    my_bookings = Booking.query.filter_by(
        user_id=user_id
    ).count()

    completed = Booking.query.filter_by(
        user_id=user_id,
        booking_status="Completed"
    ).count()

    available = Trek.query.filter_by(
        status="Open"
    ).count()

    return jsonify({

        "available_treks": available,

        "my_bookings": my_bookings,

        "completed_treks": completed

    }), 200


@trekker_bp.route("/trekker/treks", methods=["GET"])
@jwt_required()
@role_required("trekker")
def get_available_treks():

    treks = Trek.query.filter_by(
        status="Open"
    ).all()

    result = []

    for trek in treks:

        result.append({

            "id": trek.id,

            "name": trek.name,

            "location": trek.location,

            "difficulty": trek.difficulty,

            "duration": trek.duration,

            "available_slots": trek.available_slots,

            "start_date": trek.start_date,

            "end_date": trek.end_date

        })

    return jsonify(result), 200