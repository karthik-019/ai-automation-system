import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def send_email_alert(subject: str, body: str):
    print("📧 EMAIL FUNCTION CALLED")

    msg = EmailMessage()
    msg["From"] = os.getenv("EMAIL_FROM")
    msg["To"] = os.getenv("EMAIL_TO")
    msg["Subject"] = subject
    msg.set_content(body)

    host = os.getenv("EMAIL_HOST")
    port = int(os.getenv("EMAIL_PORT"))

    print(f"🔌 Connecting to SMTP {host}:{port}")

    with smtplib.SMTP(host, port) as server:
        print("🔐 Logging into SMTP")
        server.login(
            os.getenv("EMAIL_USERNAME"),
            os.getenv("EMAIL_PASSWORD")
        )
        print("📨 Sending email")
        server.send_message(msg)

    print("✅ EMAIL SENT (SMTP)")
