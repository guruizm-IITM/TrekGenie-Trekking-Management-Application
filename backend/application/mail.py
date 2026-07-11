import smtplib

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

from email.mime.base import MIMEBase

from email import encoders

import os


SMTP_SERVER = "localhost"

SMTP_PORT = 1025


def send_email(

    recipient,

    subject,

    html_body,

    attachment_path=None

):

    message = MIMEMultipart()

    message["Subject"] = subject

    message["From"] = "admin@trek.com"

    message["To"] = recipient

    message.attach(

        MIMEText(

            html_body,

            "html"

        )

    )

    if attachment_path:

        with open(

            attachment_path,

            "rb"

        ) as file:

            attachment = MIMEBase(

                "application",

                "octet-stream"

            )

            attachment.set_payload(

                file.read()

            )

            encoders.encode_base64(

                attachment

            )

            attachment.add_header(

                "Content-Disposition",

                f'attachment; filename="{os.path.basename(attachment_path)}"'

            )

            message.attach(

                attachment

            )

    with smtplib.SMTP(

        SMTP_SERVER,

        SMTP_PORT

    ) as smtp:

        smtp.send_message(

            message

        )