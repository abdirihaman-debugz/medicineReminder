import datetime
import smtplib
from email.mime.text import MIMEText
import os

# Get the current UTC time
utc_time = datetime.datetime.now(datetime.timezone.utc)

# Define the Pacific Time Zone offset (UTC-8 or UTC-7, depending on daylight saving time)
# pacific_offset = datetime.timedelta(hours=-8)  # Standard Time (UTC-8)
# If you want to consider daylight saving time, you can use:
pacific_offset = datetime.timedelta(hours=-7)  # Daylight Saving Time (UTC-7)

# Calculate the current Pacific Time
pacific_time = utc_time + pacific_offset

# Calculate the time 6 hours from the current Pacific Time
new_pacific_time = pacific_time + datetime.timedelta(hours=6)

# Format the current Pacific Time and the new time
formatted_current_time = pacific_time.strftime("%I:%M %p")
formatted_new_time = new_pacific_time.strftime("%I:%M %p")

message = "\nTIME TO TAKE YOUR MEDICINE NOW " + formatted_current_time + "\n" + "Next time you need to take your medicine: " + formatted_new_time

print(message)



# Email configuration
USER_EMAIL = os.environ.get("USER_EMAIL")
USER_PASSWORD = os.environ.get("USER_PASSWORD")
PHONE_NUMBER = os.environ.get("PHONE_NUMBER")

sender_email = USER_EMAIL
sender_password  = USER_PASSWORD

subject = "Medicine Reminder"


carrier_gateway = PHONE_NUMBER #email-to-SMS gateway

# Create a MIMEText object for the email content
msg = MIMEText(message)
msg["From"] = sender_email
msg["To"] = carrier_gateway
msg["Subject"] = subject

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



