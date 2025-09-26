import requests

SENDGRID_API_KEY = "TU_API_KEY"
FROM_EMAIL = "helltheatre@yourdomain.com"

def send_email(to_email, subject, content):
    url = "https://api.sendgrid.com/v3/mail/send"
    headers = {
        "Authorization": f"Bearer {SENDGRID_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "personalizations": [{"to": [{"email": to_email}]}],
        "from": {"email": FROM_EMAIL},
        "subject": subject,
        "content": [{"type": "text/plain", "value": content}]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.status_code
