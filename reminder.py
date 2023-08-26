import datetime
import smtplib
from email.mime.text import MIMEText
import os

old_time = datetime.datetime.now()
new_time = old_time + datetime.timedelta(hours=4, minutes=0)
message = "Medicine Reminder\nTIME TO TAKE YOUR MEDICINE NOW " + old_time.strftime("%I:%M %p" ) + " \n" + "Next time you need to take your medicine: " + new_time.strftime("%I:%M %p")
print(message)




# Email configuration
USER_EMAIL = "cronbaby2023@gmail.com"
USER_PASSWORD = "yzydscwcfjtwkveo"

sender_email = USER_EMAIL
sender_password  = USER_PASSWORD

recipient_phone = "7142669806"  # Recipient's phone number
carrier_gateway = "7142669806@tmomail.net"  # T-Mobile's email-to-SMS gateway

# Create a MIMEText object for the email content
msg = MIMEText(message)
msg["From"] = sender_email
msg["To"] = carrier_gateway

# Connect to the SMTP server
smtp_server = "smtp.gmail.com"  # Example for Gmail
smtp_port = 587  # Gmail uses port 587 for TLS

try:
    # Establish a connection to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Upgrade the connection to secure (TLS)

    # Log in to your email account
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, carrier_gateway, msg.as_string())
    server.quit()

    print("Text message sent successfully")

except Exception as e:
    print(f"An error occurred: {str(e)}")



