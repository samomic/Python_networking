# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 16:41:42 2021

Programmatically sending email. Attaching message and attachment (picture).

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
    
server.login('username@example.com', password) # enter your email address


msg = MIMEMultipart()
msg['From'] = 'Name'
msg['To'] = 'receiver@example.com' # receiver email address
msg['Subject'] = 'Hello from the python!' # subject of email message

with open('message.txt','r') as f:
    message = f.read()
    
msg.attach(MIMEText(message, 'plain'))

filename = 'Albert Einstein.jpg' # provide full path if file not in the same directory
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('sender@example.com', 'receiver@example.com', text) # successfully tested with sending from live mail to gmail
server.quit()
