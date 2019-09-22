#Enter your email and password here

USER_MAIL = input('Enter the email id (Gmail) : ') #should be in string format ex. 'example@gmail.com'
USER_PASS  = input('Enter your password : ') #shold be in string format ex. '123456'
SUBJECT = input('Enter the subject to be searched : ') #the emails you want to search from your email will contain this subject

#Do not make changes after this part

import imaplib
import base64
import os
import email

email_user = 'syedfaizan824@gmail.com' #USER_MAIL
email_pass = '9890278513' #USER_PASS

mail = imaplib.IMAP4_SSL('imap.gmail.com')

mail.login(email_user, email_pass)
mail.select('Inbox')
subject = SUBJECT
typ, data = mail.search(None,'(SUBJECT "{}")' .format(subject))
mail_ids = data[0]
id_list = mail_ids.split()

l = data[0].split()
l.reverse()

results_present = False

for i in range(len(l)):
    print(i+1,':')
    num = l[i]
    typ, data = mail.fetch(num, '(RFC822)' )
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)
    for response_part in data:
        if isinstance(response_part, tuple):
            msg = email.message_from_string(response_part[1].decode('utf-8'))
            email_subject = msg['subject']
            email_from = msg['from']
            print ('From : ' + email_from ),
            print('Date : ' + msg['Date']),
            print ('Subject : ' + email_subject + '\n')
            m = msg.get_payload(decode=True)
            if m is not None:
                m = m.decode('utf-8')
            print(m)
            print('*******************************************')
            results_present = True
    if(not results_present):
        print('No resutls found')
#logout
mail.logout()
            
