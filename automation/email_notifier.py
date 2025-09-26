import requests
import os

MAILERSEND_API_KEY = os.getenv("MAILERSEND_API_KEY", "")
FROM_EMAIL = "helltheatre@yourdomain.com"

def send_email(to_email, subject, content):
    url = "https://api.mailersend.com/v1/email"  # La nueva URL de la API de MailerSend
    headers = {
        "Authorization": f"Bearer {MAILERSEND_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "from": {"email": FROM_EMAIL},
        "to": [{"email": to_email}],
        "subject": subject,
        "text": content,
    }
    response = requests.post(url, headers=headers, json=data)
    return response.status_code