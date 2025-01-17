from dotenv import load_dotenv
import os
import imaplib
import email
load_dotenv()

username = os.getenv('USER')
password = os.getenv('PASSWORD')


def connect_to_mail():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(username, password)
    mail.select('inbox')
    return mail

def search_mail():
    mail = connect_to_mail()
    result, data = mail.search(None, '(BODY "unsubscribe")')
    data = data[0].split()

    for num in data:
        result, data = mail.fetch(num, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)
        print(email_message['From'])
        print(email_message['subject'])
        print(email_message.get_payload())

        if email_message.is_multipart():
            for part in email_message.walk():
                if part.get_content_type() == "text/html":
                    body = part.get_payload(decode=True).decode() 
                    print(body)
        else:
            content_type = email_message.get_content_type()
            body = email_message.get_payload(decode=True).decode()

            if content_type == "text/html":
                print(body)

    mail.logout()

search_mail()