
import smtplib, ssl


sender_email = input('Sender Email : ')
password = input('Sender Password : ')
receiver_email = input('Reciever Email : ')
subject = input('Enter the subject : ')
msg = input('Enter the message : ')



port = 587  # For starttls
smtp_server = "smtp.gmail.com"
message = """\
Subject: {}

{}.""" .format(subject,msg)
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
