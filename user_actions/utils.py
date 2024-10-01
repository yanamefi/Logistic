from email.mime.text import MIMEText
import smtplib
import hashlib


def send_email(body: str, recipients):
    msg = MIMEText(body)
    msg['Subject'] = 'Register confirm'
    msg['From'] = "buskomaksym08@gmail.com"
    msg['To'] = recipients
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login("buskomaksym08@gmail.com", "htgn cmqg hxgw saah")
        smtp_server.sendmail("buskomaksym08@gmail.com", recipients, msg.as_string())


def hashing(x): return hashlib.sha256(x.encode('utf-8')).hexdigest()
