import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = '<sender name>'
email['to'] = '<Recipient email address>'
email['subject'] = '<The Message>'
email.set_content('This mail was sent through python')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('<email address of the sender>','<Password>')
    smtp.send_message(email)
    print('all good ')