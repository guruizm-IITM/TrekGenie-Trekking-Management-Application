from application.extensions import db


class Trek(db.Model):

    __tablename__ = "treks"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(150), nullable=False)

    location = db.Column(db.String(150), nullable=False)

    difficulty = db.Column(db.String(50), nullable=False)

    duration = db.Column(db.Integer, nullable=False)

    available_slots = db.Column(db.Integer, nullable=False)

    status = db.Column(db.String(30), default="Open")

    assigned_staff_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    assigned_staff = db.relationship(
        "User",
        backref="assigned_treks"
    )