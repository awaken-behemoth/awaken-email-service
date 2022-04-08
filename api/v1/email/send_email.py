

import smtplib
from .Email import Email
from flask import current_app

def send_email(recipients, new_email ):
    

    smtp_host = current_app.config["EMAIL_HOST"] 
    smtp_port = current_app.config["EMAIL_PORT"]
    
    host_user = current_app.config["EMAIL_HOST_USER"] 
    host_password = current_app.config["EMAIL_HOST_PASSWORD"]
    
    
    sender_email = new_email.get_authority_email();
    
    msg = new_email.get_message()
    msg['Subject'] = new_email.get_subject();

    msg['From'] = sender_email
    
    msg['To'] = ', '.join(recipients)

    server = smtplib.SMTP_SSL(smtp_host, smtp_port)
    
    server.login(host_user, host_password)
    server.sendmail(sender_email, recipients, msg.as_string())
    
    server.quit()