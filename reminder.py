import datetime
import smtplib
from email.mime.text import MIMEText
import os

# Calculates the next time you have to take your medication
def calculate_and_format_medicine_times(hours_to_add):
    #we do this due to when the pipeline runs it use UTC and have to get the time in our current timezone
    def to_local_time():
        utc_time = datetime.datetime.now(datetime.timezone.utc)
        pacific_offset = datetime.timedelta(hours=-7)
        return utc_time + pacific_offset

    current_time = to_local_time()
    new_time = current_time + datetime.timedelta(hours=hours_to_add)

    formatted_current_time = current_time.strftime("%I:%M %p")
    formatted_new_time = new_time.strftime("%I:%M %p")

    return formatted_current_time, formatted_new_time

#Sends the email reminder
def send_reminder_message(messageToSend):
    # Email configuration
    USER_EMAIL = os.environ.get("USER_EMAIL")
    USER_PASSWORD = os.environ.get("USER_PASSWORD")
    PHONE_NUMBER = os.environ.get("PHONE_NUMBER")
    PHONE_NUMBER2 = os.environ.get("PHONE_NUMBER2")

    subject = "Medicine Reminder"

    phone_numbers = [PHONE_NUMBER, PHONE_NUMBER2]  # email-to-SMS gateway

    # Create an SMTP connection
    smtp_server = "smtp.gmail.com"  # Example for Gmail
    smtp_port = 587  # Gmail uses port 587 for TLS
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Upgrade the connection to secure (TLS)

    # Log in to your email account
    server.login(USER_EMAIL, USER_PASSWORD)

    # Message to send
    message = messageToSend

    # Send the email to each recipient
    for recipient_email in phone_numbers:
        msg = MIMEText(message)
        msg["From"] = USER_EMAIL
        msg["To"] = recipient_email
        msg["Subject"] = subject

        # Send the email
        server.sendmail(USER_EMAIL, recipient_email, msg.as_string())

    # Close the SMTP server connection
    server.quit()
    
    print("Text messages sent successfully!")

# Calculates the next time to take the medication which is 6 hours
formatted_current_time, formatted_new_time = calculate_and_format_medicine_times(6)
# Formatted message to send 
message = "\nTIME TO TAKE YOUR MEDICINE NOW:" + formatted_current_time + "\n" + "Next time you need to take your medicine: " + formatted_new_time
# Sends the reminder
send_reminder_message(message)






