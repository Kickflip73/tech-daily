#!/usr/bin/env python3
"""
J.A.R.V.I.S. Email Sender
Usage: python3 send_email.py <markdown_file> [subject]
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
PASSWORD = os.environ.get("QQ_SMTP_PASSWORD", "bfdqzfvcfimzdhdh")
RECIPIENT = "3065242502@qq.com"

def send_report(md_file: str, subject: str = None):
    content = Path(md_file).read_text(encoding="utf-8")
    
    if not subject:
        # Extract title from first line
        first_line = content.split('\n')[0].strip('# ').strip()
        subject = first_line or "J.A.R.V.I.S. Daily Report"
    
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"J.A.R.V.I.S. <{SENDER}>"
    msg["To"] = RECIPIENT
    
    msg.attach(MIMEText(content, "plain", "utf-8"))
    
    # Try to convert markdown to HTML
    try:
        import markdown
        html = markdown.markdown(content, extensions=['tables', 'fenced_code'])
        html = f"""<html><body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; line-height: 1.6;">
{html}
<hr><p style="color: #888; font-size: 12px;">—— J.A.R.V.I.S. | Stark Industries</p>
</body></html>"""
        msg.attach(MIMEText(html, "html", "utf-8"))
    except ImportError:
        pass
    
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SENDER, PASSWORD)
        server.sendmail(SENDER, RECIPIENT, msg.as_string())
    
    print(f"✅ Email sent: {subject}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 send_email.py <markdown_file> [subject]")
        sys.exit(1)
    
    md_file = sys.argv[1]
    subject = sys.argv[2] if len(sys.argv) > 2 else None
    send_report(md_file, subject)
