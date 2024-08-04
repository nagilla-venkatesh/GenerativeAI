# When an API is down for a site, this script will send an email to the site owner.

import requests
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def check_api_down():
    # Check if the API is down
    try:
        response = requests.get('https://api.example.com')
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"API is down: {e}")
        return True
    return True

