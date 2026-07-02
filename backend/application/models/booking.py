from application.extensions import db


class Booking(db.Model):

    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)

    booking_date = db.Column(
        db.DateTime,
        default=db.func.current_timestamp()
    )

    booking_status = db.Column(
        db.String(30),
        default="Booked"
    )

    payment_status = db.Column(
        db.String(30),
        default="Pending"
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    trek_id = db.Column(
        db.Integer,
        db.ForeignKey("treks.id"),
        nullable=False
    )

    user = db.relationship(
        "User",
        backref="bookings"
    )

    trek = db.relationship(
        "Trek",
        backref="bookings"
    )

    __table_args__ = (
        db.UniqueConstraint(
            "user_id",
            "trek_id",
            name="unique_booking"
        ),
    )