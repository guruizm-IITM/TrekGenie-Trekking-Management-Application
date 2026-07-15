from datetime import date, timedelta

from application import create_app
from application.extensions import db

from application.models.user import User
from application.models.trek import Trek
from application.models.booking import Booking
from application.models.staff_profile import StaffProfile


def seed_staff():

    print("Creating staff...")

    staff_members = [

        {

            "name": "Rahul Sharma",

            "email": "rahul@trekgenie.com",

            "phone": "9876543210"

        },

        {

            "name": "Priya Mehta",

            "email": "priya@trekgenie.com",

            "phone": "9876543211"

        },

        {

            "name": "Arjun Singh",

            "email": "arjun@trekgenie.com",

            "phone": "9876543212"

        }

    ]

    created = 0

    for member in staff_members:

        existing = User.query.filter_by(

            email=member["email"]

        ).first()

        if existing:

            continue

        staff = User(

            name=member["name"],

            email=member["email"],

            phone=member["phone"],

            role="staff",

            active=True

        )

        staff.set_password("staff123")

        db.session.add(staff)

        created += 1

    db.session.commit()

    print(f"{created} staff account(s) created.")



def seed_trekkers():

    print("Creating trekkers...")

    trekkers = [

        ("Amit Verma", "amit@test.com", "9876500001"),
        ("Neha Patel", "neha@test.com", "9876500002"),
        ("Rohan Desai", "rohan@test.com", "9876500003"),
        ("Sneha Joshi", "sneha@test.com", "9876500004"),
        ("Karan Shah", "karan@test.com", "9876500005"),
        ("Pooja Nair", "pooja@test.com", "9876500006"),
        ("Vikram Rao", "vikram@test.com", "9876500007"),
        ("Anjali Kulkarni", "anjali@test.com", "9876500008"),
        ("Siddharth Jain", "sid@test.com", "9876500009"),
        ("Meera Iyer", "meera@test.com", "9876500010")

    ]

    created = 0

    for name, email, phone in trekkers:

        existing = User.query.filter_by(
            email=email
        ).first()

        if existing:
            continue

        user = User(

            name=name,

            email=email,

            phone=phone,

            role="trekker",

            active=True

        )

        user.set_password("password123")

        db.session.add(user)

        created += 1

    db.session.commit()

    print(f"{created} trekker account(s) created.")



def seed_staff_profiles():

    print("Creating staff profiles...")

    profiles = [

        {

            "email": "rahul@trekgenie.com",

            "experience": 6,

            "specialization": "High Altitude Trekking"

        },

        {

            "email": "priya@trekgenie.com",

            "experience": 4,

            "specialization": "Forest Trails"

        },

        {

            "email": "arjun@trekgenie.com",

            "experience": 8,

            "specialization": "Rock Climbing"

        }

    ]

    created = 0

    for profile in profiles:

        staff = User.query.filter_by(
            email=profile["email"]
        ).first()

        if not staff:
            continue

        existing = StaffProfile.query.filter_by(
            user_id=staff.id
        ).first()

        if existing:
            continue

        staff_profile = StaffProfile(

            user_id=staff.id,

            experience=profile["experience"],

            specialization=profile["specialization"]

        )

        db.session.add(staff_profile)

        created += 1

    db.session.commit()

    print(f"{created} staff profile(s) created.")



def seed_treks():

    print("Creating treks...")

    today = date.today()

    treks = [

        {

            "name": "Kalsubai Peak",

            "location": "Ahmednagar",

            "description": "Highest peak in Maharashtra with breathtaking sunrise views.",

            "difficulty": "Moderate",

            "duration": 2,

            "available_slots": 25,

            "start_date": today + timedelta(days=1),

            "end_date": today + timedelta(days=2),

            "status": "Upcoming",

            "staff": "rahul@trekgenie.com"

        },

        {

            "name": "Rajmachi Fort",

            "location": "Lonavala",

            "description": "Historic twin forts surrounded by lush greenery.",

            "difficulty": "Easy",

            "duration": 1,

            "available_slots": 30,

            "start_date": today + timedelta(days=7),

            "end_date": today + timedelta(days=7),

            "status": "Upcoming",

            "staff": "rahul@trekgenie.com"

        },

        {

            "name": "Harishchandragad",

            "location": "Ahmednagar",

            "description": "Famous for Konkan Kada and challenging trails.",

            "difficulty": "Hard",

            "duration": 2,

            "available_slots": 20,

            "start_date": today - timedelta(days=10),

            "end_date": today - timedelta(days=8),

            "status": "Completed",

            "staff": "priya@trekgenie.com"

        },

        {

            "name": "Lohagad Fort",

            "location": "Lonavala",

            "description": "Popular beginner-friendly monsoon trek.",

            "difficulty": "Easy",

            "duration": 1,

            "available_slots": 35,

            "start_date": today + timedelta(days=14),

            "end_date": today + timedelta(days=14),

            "status": "Upcoming",

            "staff": "rahul@trekgenie.com"

        },

        {

            "name": "Visapur Fort",

            "location": "Pune",

            "description": "Scenic fort trek with waterfalls during monsoon.",

            "difficulty": "Moderate",

            "duration": 1,

            "available_slots": 30,

            "start_date": today - timedelta(days=25),

            "end_date": today - timedelta(days=24),

            "status": "Completed",

            "staff": "arjun@trekgenie.com"

        },

        {

            "name": "Torna Fort",

            "location": "Pune",

            "description": "The first fort captured by Chhatrapati Shivaji Maharaj.",

            "difficulty": "Hard",

            "duration": 2,

            "available_slots": 18,

            "start_date": today + timedelta(days=20),

            "end_date": today + timedelta(days=21),

            "status": "Upcoming",

            "staff": "arjun@trekgenie.com"

        },

        {

            "name": "Ratangad",

            "location": "Bhandardara",

            "description": "Known for the famous Nedhe (natural rock cavity).",

            "difficulty": "Moderate",

            "duration": 2,

            "available_slots": 22,

            "start_date": today + timedelta(days=30),

            "end_date": today + timedelta(days=31),

            "status": "Upcoming",

            "staff": "arjun@trekgenie.com"

        },

        {

            "name": "Sandhan Valley",

            "location": "Bhandardara",

            "description": "A thrilling valley crossing experience.",

            "difficulty": "Hard",

            "duration": 2,

            "available_slots": 15,

            "start_date": today + timedelta(days=10),

            "end_date": today + timedelta(days=11),

            "status": "Upcoming",

            "staff": "priya@trekgenie.com"

        }

    ]

    created = 0

    for item in treks:

        existing = Trek.query.filter_by(
            name=item["name"]
        ).first()

        if existing:
            continue

        staff = User.query.filter_by(
            email=item["staff"],
            role="staff"
        ).first()

        trek = Trek(

            name=item["name"],

            location=item["location"],

            description=item["description"],

            difficulty=item["difficulty"],

            duration=item["duration"],

            available_slots=item["available_slots"],

            start_date=item["start_date"],

            end_date=item["end_date"],

            status=item["status"],

            assigned_staff_id=staff.id if staff else None

        )

        db.session.add(trek)

        created += 1

    db.session.commit()

    print(f"{created} trek(s) created.")



def seed_bookings():

    print("Creating bookings...")

    bookings = [

        ("amit@test.com", "Kalsubai Peak", "Booked", "Paid"),
        ("amit@test.com", "Rajmachi Fort", "Booked", "Pending"),

        ("neha@test.com", "Harishchandragad", "Cancelled", "Pending"),
        ("neha@test.com", "Lohagad Fort", "Booked", "Paid"),

        ("rohan@test.com", "Visapur Fort", "Booked", "Paid"),
        ("rohan@test.com", "Torna Fort", "Booked", "Pending"),

        ("sneha@test.com", "Ratangad", "Booked", "Paid"),
        ("sneha@test.com", "Sandhan Valley", "Booked", "Pending"),

        ("karan@test.com", "Kalsubai Peak", "Booked", "Paid"),
        ("karan@test.com", "Rajmachi Fort", "Booked", "Paid"),

        ("pooja@test.com", "Harishchandragad", "Booked", "Pending"),
        ("pooja@test.com", "Lohagad Fort", "Cancelled", "Pending"),

        ("vikram@test.com", "Visapur Fort", "Booked", "Paid"),
        ("vikram@test.com", "Torna Fort", "Booked", "Paid"),

        ("anjali@test.com", "Ratangad", "Booked", "Pending"),
        ("anjali@test.com", "Sandhan Valley", "Booked", "Paid"),

        ("sid@test.com", "Kalsubai Peak", "Booked", "Paid"),
        ("sid@test.com", "Lohagad Fort", "Booked", "Pending"),

        ("meera@test.com", "Rajmachi Fort", "Booked", "Paid"),
        ("meera@test.com", "Ratangad", "Booked", "Paid")

    ]

    created = 0

    for email, trek_name, booking_status, payment_status in bookings:

        user = User.query.filter_by(
            email=email
        ).first()

        trek = Trek.query.filter_by(
            name=trek_name
        ).first()

        if not user or not trek:
            continue

        existing = Booking.query.filter_by(
            user_id=user.id,
            trek_id=trek.id
        ).first()

        if existing:
            continue

        booking = Booking(

            user_id=user.id,

            trek_id=trek.id,

            booking_status=booking_status,

            payment_status=payment_status

        )

        db.session.add(booking)

        created += 1

    db.session.commit()

    print(f"{created} booking(s) created.")



def print_summary():

    print("\n======================================")

    print("🏔 TrekGenie Demo Data Created")

    print("======================================")

    print("Admin")
    print("admin@trekgenie.com")
    print("admin123\n")

    print("Staff")
    print("rahul@trekgenie.com")
    print("staff123\n")

    print("Trekker")
    print("amit@test.com")
    print("password123")

    print("======================================")



def seed_demo_data():

    seed_staff()

    seed_trekkers()

    seed_staff_profiles()

    seed_treks()

    seed_bookings()

    db.session.commit()

    print_summary()



if __name__ == "__main__":

    app = create_app()

    with app.app_context():

        seed_demo_data()