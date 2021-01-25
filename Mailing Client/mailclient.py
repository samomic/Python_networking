# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 16:41:42 2021

@author: Samir
"""

import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


server = smtplib.SMTP('smtp.example.com', 587) # use port 587, timeout error if using standard port 25
 
server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()  # ideally should encrypt and decrypt password from file

server.starttls() # encrypting smtp session
server.ehlo()
    
server.login('username@example.com', password)


msg = MIMEMultipart()
msg['From'] = 'Name'
msg['To'] = 'receiver@example.com'
msg['Subject'] = 'Hello from the hotmail!'

with open('message.txt','r') as f:
    message = f.read()
    
msg.attach(MIMEText(message, 'plain'))

filename = 'Albert Einstein.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('sender@example.com', 'receiver@example.com', text) # tested with sending from live mail to gmail
server.quit()
