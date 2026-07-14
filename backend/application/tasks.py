from datetime import date, timedelta

from sqlalchemy import func

from application.extensions import celery, db
from application.exports import generate_booking_csv
from application.mail import send_email
from application.models import User, Trek, Booking


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

        subject="Your TrekGenie Booking History",

        html_body="""
        <h2>🏔 TrekGenie</h2>

        <p>Hello,</p>

        <p>
        Your booking history has been successfully exported.
        </p>

        <p>
        Please find the attached CSV file containing your booking history.
        </p>

        <p>
        Thank you for choosing <b>TrekGenie</b>.
        We look forward to helping you plan your next adventure!
        </p>

        <br>

        <p>
        Regards,<br>
        <b>TrekGenie Team</b><br>
        Adventure Begins Here.
        </p>

        <hr>

        <small style="color:gray;">
        This is an automated email from TrekGenie.
        Please do not reply to this email.
        </small>
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

            subject="🏔 Trek Reminder - TrekGenie",

            html_body=f"""
            <h2>🏔 TrekGenie</h2>

            <p>Hello {booking.user.name},</p>

            <p>
            Your adventure begins tomorrow!
            This is a friendly reminder for your upcoming trek.
            </p>

            <hr>

            <p>

            <b>Trek:</b> {booking.trek.name}<br>

            <b>Location:</b> {booking.trek.location}<br>

            <b>Start Date:</b> {booking.trek.start_date}<br>

            <b>Booking Status:</b> {booking.booking_status}<br>

            <b>Payment Status:</b> {booking.payment_status}

            </p>

            <hr>

            <h3>Things to Carry</h3>

            <ul>

                <li>Water Bottle</li>

                <li>Government Photo ID</li>

                <li>Trekking Shoes</li>

                <li>Rain Protection (if required)</li>

            </ul>

            <p>

            Please arrive at the reporting location at least
            <b>30 minutes before departure.</b>

            </p>

            <p>

            We wish you a safe and memorable trekking experience.

            Happy Trekking!

            </p>

            <br>

            <p>

            Regards,<br>

            <b>TrekGenie Team</b><br>

            Adventure Begins Here.

            </p>

            <hr>

            <small style="color:gray;">

            This is an automated email from TrekGenie.

            Please do not reply to this email.

            </small>
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

    <h2>🏔 TrekGenie</h2>

    <p>Hello Administrator,</p>

    <p>

    Please find below your monthly trekking activity summary.

    </p>

    <hr>

    <p><b>Total Treks Conducted:</b> {total_treks}</p>

    <p><b>Total Participants:</b> {total_users}</p>

    <p><b>Total Bookings:</b> {total_bookings}</p>

    <p><b>Most Popular Trek:</b> {popular_name}</p>

    <p><b>Total Bookings for Most Popular Trek:</b> {popular_count}</p>

    <hr>

    <p>

    This report has been generated automatically by the
    TrekGenie reporting system.

    </p>

    <br>

    <p>

    Regards,<br>

    <b>TrekGenie Team</b><br>

    Adventure Begins Here.

    </p>

    <hr>

    <small style="color:gray;">

    This is an automated email from TrekGenie.

    Please do not reply to this email.

    </small>

    """

    send_email(

        recipient="admin@trekgenie.com",

        subject="🏔 Monthly TrekGenie Activity Report",

        html_body=html

    )

    return "Monthly report sent."