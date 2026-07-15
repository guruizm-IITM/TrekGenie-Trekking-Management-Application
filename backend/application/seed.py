from application.extensions import db
from application.models import User


def create_admin():

    admin = User.query.filter_by(
        email="admin@trekgenie.com"
    ).first()

    if admin is None:

        admin = User(
            name="Administrator",
            email="admin@trekgenie.com",
            role="admin",
            phone="9999999999"
        )

        admin.set_password("admin123")

        db.session.add(admin)

        db.session.commit()