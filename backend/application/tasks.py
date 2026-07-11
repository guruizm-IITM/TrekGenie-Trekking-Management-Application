from application.extensions import celery

from application.extensions import db

from application.models import User

from application.exports import generate_booking_csv

from application.mail import send_email

from datetime import date, timedelta

from application.models import Booking, Trek


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


@celery.task
def send_daily_reminders():

    tomorrow = date.today() + timedelta(days=1)

    bookings = (
        Booking.query
        .join(Trek)
        .filter(
            Trek.start_date == tomorrow,
            Booking.booking_status == "Booked"
        )
        .all()
    )

    for booking in bookings:

        send_email(

            recipient=booking.user.email,

            subject="Upcoming Trek Reminder",

            html_body=f"""
            <h2>Your trek starts tomorrow!</h2>

            <p><b>Trek:</b> {booking.trek.name}</p>

            <p><b>Location:</b> {booking.trek.location}</p>

            <p><b>Start Date:</b> {booking.trek.start_date}</p>

            <br>

            <h3>Things to carry</h3>

            <ul>
                <li>Water Bottle</li>
                <li>ID Proof</li>
                <li>Trekking Shoes</li>
                <li>Rain Protection (if required)</li>
            </ul>

            <p>Happy Trekking!</p>
            """

        )

    return f"{len(bookings)} reminder(s) sent."