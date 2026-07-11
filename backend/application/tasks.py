from application.extensions import celery

from application.extensions import db

from application.models import User

from application.exports import generate_booking_csv

from application.mail import send_email


@celery.task
def test_task():

    print("Celery is working!")

    return "Success"


@celery.task
def export_booking_history(user_id):

    user = db.session.get(User, user_id)

    if not user:

        return "User not found."

    csv_file = generate_booking_csv(user_id)

    send_email(

        recipient=user.email,

        subject="Your Booking History",

        html_body="""
        <h2>Booking History Export</h2>

        <p>Your booking history has been exported successfully.</p>

        <p>Please find the attached CSV.</p>

        <p>Happy Trekking!</p>
        """,

        attachment_path=csv_file

    )

    return "Export completed successfully."