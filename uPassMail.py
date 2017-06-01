import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

username = 'throwawayGmailUsername'
password = 'throwawayGmailPassword'

def initializeEmail():
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(username,password)
    return s

def sendEmail(s, message, attachments):
    msg = MIMEMultipart()

    msg['From'] = username
    msg['To'] = "yourGmailUsername"
    msg['Subject']="uPass Updated"

    for attachment in attachments:
        img = MIMEImage(attachment.read())
        attachment.close()
        msg.attach(img)

    msg.attach(MIMEText(message, 'plain'))

    s.send_message(msg)

    del msg
