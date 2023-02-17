import os
from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'swapnilpatil46117@gmail.com'
email_password = os.environ.get("EMAIL_PASSWORD")
email_receiver = 'navanathgaikwad7010@gmail.com'

subject = "Automation mail sender by using python."
body = """
Hii, iam swapnil patil.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
	try :
		smtp.login(email_sender, email_password)
		smtp.sendmail(email_sender, email_receiver, em.as_string())
	except smtplib.SMTPResponseException:
		print("Errored")
