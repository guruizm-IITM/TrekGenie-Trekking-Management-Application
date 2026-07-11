from application.extensions import celery

from application.extensions import db

from application.models import User, Trek, Booking

from application.exports import generate_booking_csv

from application.mail import send_email

from datetime import date, timedelta

from application.models import Booking, Trek

from sqlalchemy import func


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

@celery.task
def send_monthly_report():

    total_treks = Trek.query.count()

    total_bookings = Booking.query.count()

    total_users = (
        db.session.query(
            func.count(
                func.distinct(
                    Booking.user_id
                )
            )
        ).scalar()
    )

    popular = (
        db.session.query(

            Trek.name,

            func.count(
                Booking.id
            ).label("bookings")

        )
        .join(Booking)
        .group_by(Trek.id)
        .order_by(
            func.count(
                Booking.id
            ).desc()
        )
        .first()
    )

    popular_name = "N/A"

    popular_count = 0

    if popular:

        popular_name = popular[0]

        popular_count = popular[1]

    html = f"""

    <h1>🏔 Monthly Trekking Report</h1>

    <hr>

    <p><b>Total Treks Conducted:</b> {total_treks}</p>

    <p><b>Total Participants:</b> {total_users}</p>

    <p><b>Total Bookings:</b> {total_bookings}</p>

    <p><b>Most Popular Trek:</b> {popular_name}</p>

    <p><b>Total Bookings:</b> {popular_count}</p>

    <hr>

    <p>Generated automatically using Celery.</p>

    """

    send_email(

        recipient="admin@trek.com",

        subject="Monthly Trekking Activity Report",

        html_body=html

    )

    return "Monthly report sent."