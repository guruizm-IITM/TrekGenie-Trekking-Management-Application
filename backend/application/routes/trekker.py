from flask import Blueprint, jsonify, request
from application.extensions import cache

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
@cache.cached(timeout=300, query_string=True)
def get_available_treks():

    name = request.args.get("name")
    location = request.args.get("location")
    difficulty = request.args.get("difficulty")
    duration = request.args.get("duration")

    treks = Trek.query.filter_by(
        status="Open"
    )

    if name:

        treks = treks.filter(
            Trek.name.ilike(f"%{name}%")
        )

    if location:

        treks = treks.filter(
            Trek.location.ilike(f"%{location}%")
        )

    if difficulty:

        treks = treks.filter_by(
            difficulty=difficulty
        )

    if duration:

        try:

            treks = treks.filter_by(
                duration=int(duration)
            )

        except ValueError:

            return jsonify({
                "message": "Duration must be a number."
            }), 400

    treks = treks.all()

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

@trekker_bp.route("/trekker/bookings", methods=["POST"])
@jwt_required()
@role_required("trekker")
def book_trek():

    user_id = int(get_jwt_identity())

    data = request.get_json()

    if "trek_id" not in data:
        return jsonify({
            "message": "trek_id is required."
        }), 400

    trek = db.session.get(Trek, data["trek_id"])

    if not trek:
        return jsonify({
            "message": "Trek not found."
        }), 404

    if trek.status != "Open":
        return jsonify({
            "message": "This trek is not open for booking."
        }), 400

    if trek.available_slots <= 0:
        return jsonify({
            "message": "No slots available."
        }), 400

    existing_booking = Booking.query.filter_by(
        user_id=user_id,
        trek_id=trek.id
    ).first()

    if existing_booking:
        return jsonify({
            "message": "You have already booked this trek."
        }), 409

    booking = Booking(
        user_id=user_id,
        trek_id=trek.id
    )

    trek.available_slots -= 1

    db.session.add(booking)

    db.session.commit()

    return jsonify({
        "message": "Trek booked successfully."
    }), 201


@trekker_bp.route("/trekker/bookings", methods=["GET"])
@jwt_required()
@role_required("trekker")
def booking_history():

    user_id = int(get_jwt_identity())

    bookings = Booking.query.filter_by(
        user_id=user_id
    ).all()

    result = []

    for booking in bookings:

        result.append({

            "booking_id": booking.id,

            "trek_name": booking.trek.name,

            "location": booking.trek.location,

            "booking_status": booking.booking_status,

            "payment_status": booking.payment_status,

            "booking_date": booking.booking_date

        })

    return jsonify(result), 200


@trekker_bp.route("/trekker/bookings/<int:booking_id>/cancel", methods=["PATCH"])
@jwt_required()
@role_required("trekker")
def cancel_booking(booking_id):

    user_id = int(get_jwt_identity())

    booking = Booking.query.filter_by(
        id=booking_id,
        user_id=user_id
    ).first()

    if not booking:
        return jsonify({
            "message": "Booking not found."
        }), 404

    if booking.booking_status == "Cancelled":
        return jsonify({
            "message": "Booking already cancelled."
        }), 400

    booking.booking_status = "Cancelled"

    booking.trek.available_slots += 1

    db.session.commit()

    return jsonify({
        "message": "Booking cancelled successfully."
    }), 200

@trekker_bp.route("/trekker/profile", methods=["GET"])
@jwt_required()
@role_required("trekker")
def get_profile():

    user_id = int(get_jwt_identity())

    user = db.session.get(User, user_id)

    return jsonify({

        "name": user.name,

        "email": user.email,

        "phone": user.phone

    }), 200

@trekker_bp.route("/trekker/profile", methods=["PATCH"])
@jwt_required()
@role_required("trekker")
def update_profile():

    user_id = int(get_jwt_identity())

    user = db.session.get(User, user_id)

    data = request.get_json()

    if "name" in data:

        user.name = data["name"]

    if "phone" in data:

        user.phone = data["phone"]

    db.session.commit()

    return jsonify({

        "message": "Profile updated successfully."

    }), 200


@trekker_bp.route("/trekker/export", methods=["POST"])
@jwt_required()
@role_required("trekker")
def export_history():

    user_id = int(get_jwt_identity())

    from application.tasks import export_booking_history

    export_booking_history.delay(user_id)

    return jsonify({

        "message": "Booking history export started."

    }), 202