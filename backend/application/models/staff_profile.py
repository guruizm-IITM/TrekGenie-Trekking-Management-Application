from application.extensions import db


class StaffProfile(db.Model):

    __tablename__ = "staff_profiles"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
        unique=True
    )

    experience = db.Column(db.Integer, default=0)

    specialization = db.Column(db.String(100))

    user = db.relationship(
        "User",
        backref="staff_profile"
    )