import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

old_time = datetime.datetime.now()
new_time = old_time + datetime.timedelta(hours=6, minutes=0)
message = "TIME TO TAKE YOUR MEDICINE NOW " + old_time.strftime("%I:%M %p" ) + " \n" + "Next time you need to take your medicine: " + new_time.strftime("%I:%M %p")
print(message)




# Email configuration
USER_EMAIL = os.environ.get("USER_EMAIL")
USER_PASSWORD = os.environ.get("USER_PASSWORD")
sender_email = USER_EMAIL
receiver_email = USER_EMAIL  # Use the same email address for sender and receiver
password = USER_PASSWORD
subject = "Medicine Reminder"

# Create a MIMEText object for the email content
email_body = MIMEMultipart()
email_body.attach(MIMEText(message, "plain"))

# Set the email headers
email_body["From"] = sender_email
email_body["To"] = receiver_email
email_body["Subject"] = subject

# Connect to the SMTP server
smtp_server = "smtp.gmail.com"  # Example for Gmail
smtp_port = 587  # Gmail uses port 587 for TLS

try:
    # Establish a connection to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Upgrade the connection to secure (TLS)

    # Log in to your email account
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, receiver_email, email_body.as_string())

    # Close the SMTP server connection
    server.quit()
    print("Email sent successfully!")

except Exception as e:
    print(f"An error occurred: {str(e)}")
