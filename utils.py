import sqlite3
import hashlib
import smtplib
from email.mime.text import MIMEText
import random


conn = sqlite3.connect("database.db")
cursor = conn.cursor()

conn.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    full_name TEXT,
    user_name TEXT UNIQUE,
    password TEXT NOT NULL,
    photo TEXT DEFAULT 'avatar.png'
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    item TEXT,
    quantity INTEGER,
    time TEXT,
    mode TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS registrations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    expiration TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS reservations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    date TEXT,
    class TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
""")
               
conn.commit()
conn.close()

class Application:
    def __init__(self, email, fullname, password, otp):
        self.email = email
        self.fullname = fullname
        self.password = password 
        self.sender_email_address  = "" # company email address here
        self.sender_email_pass = "" # company email pass here
        self.otp = otp

    def hash(self):
        return hashlib.sha256(self.password.encode()).hexdigest()

    def send_email(self, subject, body):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.sender_email_address
        msg['To'] = self.email
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(self.sender_email_address, self.sender_email_pass)
        server.sendmail(self.sender_email_address, self.email, msg.as_string())
        server.quit()

    def send_otp(self):
        otp = "".join(str(random.randint(0, 9)) for _ in range(6))
        subject = 'FORTUNATE HUB TAIWO ISALE ILORIN'
        body = f"""{otp} is your FORTUNATE HUB One-Time-Passcode for email verification.

    Copy and paste the code {otp} to complete your account registration.

    For your security, do not share this code with anyone.

    If you did not request this code, you can simply ignore this email."""
        Application.send_email(receiver_email_address=self.email, suBject=subject, body=body)
        return otp

    def verify(self):
            otp = Application.send_otp(self.email)
            if self.otp == otp:
                Application.register(self)
            else: 
                return 1

    def register(self):
        try:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()

            cursor.execute("""
            INSERT INTO users (email, full_name, password)
            VALUES (?, ?, ?)
            """, (self.email, self.full_name, hash(self.password)))

            conn.commit()
            return 0

        except sqlite3.IntegrityError:
            return 1

        finally:
            conn.close()

    def authenticate(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("SELECT password FROM users WHERE email = ?", (self.email,))
        result = cursor.fetchone()

        conn.close()

        if result is None:
            return f"No registered user for {self.email}"

        stored_password = result[0]
        if stored_password == hash(self.password):
            return 0
        else:
            return 1