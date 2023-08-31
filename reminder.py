import datetime
import smtplib
from email.mime.text import MIMEText
import os



USER_EMAIL = os.environ.get("USER_EMAIL")
USER_PASSWORD = os.environ.get("USER_PASSWORD")
PHONE_NUMBERS = os.environ.get("PHONE_NUMBERS")
# PHONE_NUMBER2 = os.environ.get("PHONE_NUMBER2")
# phone_numbers = [PHONE_NUMBER, PHONE_NUMBER2]
subject = "Medicine Reminder"

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

#Sends the text reminder
def send_reminder_message(email, password, phoneArr, subjectToSend, messageToSend):

    # Create an SMTP connection
    smtp_server = "smtp.gmail.com"  # smtp for Gmail
    smtp_port = 587  # Gmail uses port 587 for TLS
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Upgrade the connection to secure (TLS)

    # Log in to your email account
    server.login(email, password)

    # Send the text to each recipient (EMAIL to SMS)
    for recipient_email in phoneArr:
        print(recipient_email)
        msg = MIMEText(messageToSend)
        msg["From"] = USER_EMAIL
        msg["To"] = recipient_email
        msg["Subject"] = subjectToSend

        # Sends the text
        server.sendmail(USER_EMAIL, recipient_email, msg.as_string())

    # Close the SMTP server connection
    server.quit()
    
    print("Text messages sent successfully!")

# Calculates the next time to take the medication which is 6 hours
formatted_current_time, formatted_new_time = calculate_and_format_medicine_times(6)
# Formatted message to send 
message = "\nTIME TO TAKE YOUR MEDICINE NOW:" + formatted_current_time + "\n" + "Next time you need to take your medicine: " + formatted_new_time
# Sends the reminder
send_reminder_message(USER_EMAIL, USER_PASSWORD, PHONE_NUMBERS, subject,  message)



