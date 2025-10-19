import smtplib, os, json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
TO_EMAIL = os.getenv("TO_EMAIL") or EMAIL_USER
JSON_FILE = "blackboard_data.json"

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = TO_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)
    print(f"Email sent: {subject}")

def load_data():
    if not os.path.exists(JSON_FILE):
        return {"notified": []}
    try:
        with open(JSON_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {"notified": []}

def save_data(data):
    with open(JSON_FILE, "w") as f:
        json.dump(data, f, indent=4)

def has_been_notified(item_name):
    data = load_data()
    return item_name in data.get("notified", [])

def mark_as_notified(item_name):
    data = load_data()
    if "notified" not in data:
        data["notified"] = []
    if item_name not in data["notified"]:
        data["notified"].append(item_name)
    save_data(data)

def is_within_4_hours(deadline):
    if isinstance(deadline, str):
        deadline = datetime.strptime(deadline, "%Y-%m-%d %H:%M")
    now = datetime.now()
    diff = deadline - now
    return timedelta(hours=0) < diff <= timedelta(hours=4)

def notify_updates(new_items, deadlines):
    for item in new_items:
        if not has_been_notified(item):
            send_email("New Blackboard Content", f"New content uploaded: {item}")
            mark_as_notified(item)
    for assignment, deadline in deadlines.items():
        if is_within_4_hours(deadline) and not has_been_notified(assignment):
            send_email("Upcoming Deadline", f"'{assignment}' is due soon! Deadline: {deadline}")
            mark_as_notified(assignment)
