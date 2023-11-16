"""
Sends a pun from a text file via email.
Private info is stored as environment variables.
The script is run everyday using CRON. 
"""

import os
import smtplib
from datetime import datetime

def get_index():
    # Selects pun based on day
    start_epoch = datetime(2023, 11, 16)
    now = datetime.now()
    return int((now - start_epoch).days)

def get_pun(idx):
    punfile = os.environ.get('PUN_PATH') + 'puns.txt'
    with open(punfile, 'r', encoding='utf-8') as f:
        puns = f.readlines()
    return puns[idx]

def send_email(pun, recipients):
    subject = 'Pun of the day'
    body = f"Bleep your daily pun has been generated bloop:\n\n{pun}"
    message = f"Subject: {subject}\n\n{body}"

    # Connect to the SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender = os.environ.get('GMAIL_USERNAME')
    app_pswd = os.environ.get('GMAIL_APP_PASSWORD')
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender, app_pswd)
        server.sendmail(sender, recipients, message)
        server.quit()

def main():
    recipients = os.environ.get('RECIPIENTS', '').split(',')
    idx = get_index()
    pun = get_pun(idx)
    send_email(pun, recipients)

if __name__ == '__main__':
    main()