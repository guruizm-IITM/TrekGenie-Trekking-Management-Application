import csv
import os

from application.models import Booking


BASE_DIR = os.getcwd()

EXPORT_FOLDER = os.path.join(
    BASE_DIR,
    "exports"
)


def generate_booking_csv(user_id):

    if not os.path.exists(EXPORT_FOLDER):

        os.makedirs(EXPORT_FOLDER)

    filename = f"booking_history_{user_id}.csv"

    filepath = os.path.join(

        EXPORT_FOLDER,

        filename

    )

    bookings = Booking.query.filter_by(

        user_id=user_id

    ).all()

    with open(

        filepath,

        "w",

        newline=""

    ) as file:

        writer = csv.writer(file)

        writer.writerow([

            "User ID",

            "Trek Name",

            "Location",

            "Booking Status",

            "Booking Date"

        ])

        for booking in bookings:

            writer.writerow([

                booking.user.id,

                booking.trek.name,

                booking.trek.location,

                booking.booking_status,

                booking.booking_date

            ])

    return filepath