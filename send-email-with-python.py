import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up the email sender, receiver, and login credentials
sender_email = "harshj86683@gmail.com"
receiver_email = "harshj86683@gmail.com"
password = "YOUR PASSWORD"

# Create the email subject and body
subject = "Test Email"
body = "This is a test email sent from Python."

# Set up the MIME object
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach the body text to the MIME object
msg.attach(MIMEText(body, 'plain'))

# Connect to the Gmail SMTP server and send the email
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
finally:
    server.quit()
