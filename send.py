import pandas as pd
import smtplib
import time
import random
import os
from email.message import EmailMessage
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# =====================================================
# GMAIL DETAILS
# =====================================================
EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

if not EMAIL or not APP_PASSWORD:
    raise ValueError("EMAIL or APP_PASSWORD not set in environment variables/ .env file")


# =====================================================
# FILES
# =====================================================
EXCEL_FILE = "sample_emails.xlsx"
TEMPLATE_FILE = "email_template.txt"
RESUME_FILE = "sample_resume.pdf"

# =====================================================
# READ EXCEL
# =====================================================
df = pd.read_excel(EXCEL_FILE)

# =====================================================
# READ EMAIL TEMPLATE
# (Do NOT include "Subject:" inside this file)
# =====================================================
with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
    template = f.read()

# =====================================================
# CONNECT TO GMAIL
# =====================================================
server = smtplib.SMTP("smtp.gmail.com", 587, timeout=30)
server.ehlo()
server.starttls()
server.ehlo()
server.login(EMAIL, APP_PASSWORD)

print("=" * 60)
print("Logged in successfully!")
print("=" * 60)

sent_emails = set()

total = len(df)
success = 0
failed = 0
skipped = 0

# =====================================================
# SEND EMAILS
# =====================================================
for index, row in df.iterrows():

    # --------------------------
    # EMAIL
    # --------------------------
    email = str(row["Email"]).strip()

    if email == "" or email.lower() == "nan":
        skipped += 1
        print(f"[{index+1}/{total}] Skipped Empty Email")
        continue

    if email in sent_emails:
        skipped += 1
        print(f"[{index+1}/{total}] Duplicate Email -> {email}")
        continue

    sent_emails.add(email)

    # --------------------------
    # PLACEHOLDERS
    # --------------------------
    name = (
        str(row["Name"]).strip()
        if "Name" in df.columns and pd.notna(row["Name"])
        else "Hiring Team"
    )

    company = (
        str(row["Company"]).strip()
        if "Company" in df.columns and pd.notna(row["Company"])
        else "Your Company"
    )

    role = (
        str(row["Role"]).strip()
        if "Role" in df.columns and pd.notna(row["Role"])
        else "Software Development Engineer"
    )

    # --------------------------
    # EMAIL BODY
    # --------------------------
    body = template.format(
        name=name,
        company=company,
        role=role,
    )

    # --------------------------
    # SUBJECT
    # --------------------------
    sender_name = os.getenv("SENDER_NAME", "Your Name")
    subject = f"Looking to Build, Solve & Contribute at {company} | {sender_name}"

    # --------------------------
    # CREATE EMAIL
    # --------------------------
    msg = EmailMessage()

    msg["From"] = f"{sender_name} <{EMAIL}>"
    msg["To"] = email
    msg["Subject"] = subject

    msg.set_content(body)

    # --------------------------
    # ATTACH RESUME
    # --------------------------
    try:
        with open(RESUME_FILE, "rb") as file:
            msg.add_attachment(
                file.read(),
                maintype="application",
                subtype="pdf",
                filename="Mohd_Kaif_Resume.pdf",
            )
    except FileNotFoundError:
        print(f"Resume file not found: {RESUME_FILE}")
        break

    # --------------------------
    # SEND EMAIL
    # --------------------------
    try:
        server.send_message(msg)
        success += 1
        print(f"[{index+1}/{total}] ✅ Sent -> {email}")

    except Exception as e:
        failed += 1
        print(f"[{index+1}/{total}] ❌ Failed -> {email}")
        print(e)

    # --------------------------
    # RANDOM DELAY
    # --------------------------
    delay = random.randint(2, 5)
    print(f"Waiting {delay} seconds...\n")
    time.sleep(delay)

# =====================================================
# CLOSE CONNECTION
# =====================================================
server.quit()

# =====================================================
# SUMMARY
# =====================================================
print("\n" + "=" * 60)
print("Email Sending Completed")
print("=" * 60)
print(f"Total Emails : {total}")
print(f"Sent         : {success}")
print(f"Failed       : {failed}")
print(f"Skipped      : {skipped}")
print("=" * 60)