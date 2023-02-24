import logging
import os
import argparse
from flask import Flask
import smtplib
from email.message import EmailMessage
from datetime import datetime

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)

def sendEmail(subject, body):
    APP_EMAIL=os.getenv("EMAIL")
    APP_PASSWORD=os.getenv("PASSWORD")

    email = EmailMessage()
    email["From"] = APP_EMAIL
    email["To"] = ["xyz@gmail.com"]
    email["Subject"] = subject
    email.set_content(body)
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(APP_EMAIL, APP_PASSWORD)
        smtp.send_message(email)

@app.route('/')
def home():
    return f"Hello World from {int(args.port)} with {int(args.idletime)} through {args.instanceid}"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--idletime", help="How many seconds of idle time before cut audio into chunk.")
    parser.add_argument("--port", help="Port")
    parser.add_argument("--instanceid", help="instanceid")
    args = parser.parse_args()

    app.run(port=int(args.port))
    with app.app_context():
        subject = f"Warning! Service Crash or Stop - Service: service-example | {args.instanceid}"
        body = f"Service Crash or Stop for service-example.py with information details below:\nDatetime: {datetime.now()}\nInstance ID: {args.instanceid}\nPort: {args.port}\nIdletime: {args.idletime}"
        sendEmail(subject, body)