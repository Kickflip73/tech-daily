#!/usr/bin/env python3
"""
J.A.R.V.I.S. HTML Email Sender
Send a pre-built HTML email file via QQ SMTP (SSL port 465)
Usage: QQ_SMTP_PASSWORD=xxx python3 send_html_email.py <html_file> <subject>
"""
import sys
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path

SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 465
SENDER = "3065242502@qq.com"
RECIPIENT = "3065242502@qq.com"


def send_html_email(html_file: str, subject: str):
    password = os.environ.get("QQ_SMTP_PASSWORD", "").strip()
    if not password:
        print("ERROR: QQ_SMTP_PASSWORD environment variable not set", file=sys.stderr)
        sys.exit(1)

    html_content = Path(html_file).read_text(encoding="utf-8")

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"J.A.R.V.I.S. <{SENDER}>"
    msg["To"] = RECIPIENT
    msg["X-Mailer"] = "JARVIS-Tech-Intelligence-System/1.0"

    # Plain text fallback
    plain_text = "请使用支持 HTML 的邮件客户端查看此报告。J.A.R.V.I.S. 技术情报系统"
    msg.attach(MIMEText(plain_text, "plain", "utf-8"))
    msg.attach(MIMEText(html_content, "html", "utf-8"))

    print(f"Connecting to {SMTP_SERVER}:{SMTP_PORT} ...")
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SENDER, password)
        server.sendmail(SENDER, RECIPIENT, msg.as_string())

    print(f"✅ Email sent successfully!")
    print(f"   From: {SENDER}")
    print(f"   To:   {RECIPIENT}")
    print(f"   Subject: {subject}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 send_html_email.py <html_file> <subject>")
        sys.exit(1)
    send_html_email(sys.argv[1], sys.argv[2])
