

import smtplib
from flask import current_app
from email.mime.text import MIMEText

from .get_authority_email import get_authority_email



def send_email(recipients,email ,authority):
    

    smtp_host = current_app.config["EMAIL_HOST"] 
    smtp_port = current_app.config["EMAIL_PORT"]
    
    host_user = current_app.config["EMAIL_HOST_USER"] 
    host_password = current_app.config["EMAIL_HOST_PASSWORD"]
    
    sender_email = get_authority_email(authority);
    

    msg = MIMEText('Hi, how are you today?')
    msg['Subject'] = email.subject
    msg['From'] = sender_email
    
    msg['To'] = ', '.join(recipients)

    server = smtplib.SMTP_SSL(smtp_host, smtp_port)
    
    server.login(host_user, host_password)
    server.sendmail(sender_email, recipients, msg.as_string())
    
    server.quit()