import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os

'''
Given the image paths from the generated images, send an email to the user with the images as attachments
email: str - The email address to send the images to
password: str - The password for the email account
image_paths: list[str] - The paths to the images to send
'''
def send_email(email, password, image_paths):

    # Email configuration
    sender_email = email # user will be sending email to themselves
    sender_password = password
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = email
    message["Subject"] = "Generated Images"

    # Add text body
    body = "Here are your generated images:"
    message.attach(MIMEText(body, "plain"))

    # Attach images
    for image_path in image_paths:
        with open(image_path, "rb") as image_file:
            image = MIMEImage(image_file.read(), name=os.path.basename(image_path))
            message.attach(image)

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
        print(f"Email sent successfully to {email}")
    except Exception as e:
        print(f"Error sending email: {str(e)}")

__all__ = ["send_email"]