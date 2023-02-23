import os
import imghdr
import smtplib
import pandas as pd
import seaborn as sns
from email.message import EmailMessage
from email.mime.image import MIMEImage

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('swapnilpatil46117@gmail.com', 'xvfxeadltnyzbfxj')

email = EmailMessage()
email['From'] = 'swapnilpatil46117@gmail.com'
email ['To'] = 'navanathgaikwad7010@gmail.com'
email['Subject'] = 'Automation Application'
email.set_content("Auto mail sender application_graph image in python.")
server.send_message(email)

with open('Bappa.png', 'rb') as f:
	img_data = f.read()
	img_type = imghdr.what(f.name)
	img_name = f.name

email.add_attachment(img_data, maintype='image', subtype='image_type', filename='image_name')



"""
    file_data = imeg.name
    file_type = imghdr.what('Bappa.png')
    file_name = imeg.name
email.add_attachment(file_data, subtype = file_type, filename = file_name)
"""