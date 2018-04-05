# import MySQLdb
import httplib2
import os
import oauth2client
from oauth2client import client, tools
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from apiclient import errors, discovery
import mimetypes
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase

SCOPES = 'https://www.googleapis.com/auth/gmail.send'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'gmail_service'

# def database():
#   db = MySQLdb.connect(host="188.166.245.69", 
#           user="wgDashProdUser", 
#           passwd="w1k4gedung", 
#           db="wg_dashboard_production")
#   cursor = db.cursor()
#   query = "SELECT email FROM db_mobile_user"
#   cursor.execute(query)
#   db.commit()

#   numrows = cursor.rowcount
#   emailUser = ""
#   for x in range(0, numrows):
#     row = cursor.fetchone()
#     email = row[0]
#     if (emailUser == ""):
#       emailUser = str(email)
#     else :
#       emailUser = str(emailUser) + ", " + str(email)
#   return str(emailUser)
#   db.close()

def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-python-email-send.json')
    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow, store)
        print 'Storing credentials to ' + credential_path
    return credentials

def SendMessage(sender, to, subject, msgPlain, attachmentFile=None):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    message1 = CreateMessage(sender, to, subject,  msgPlain)
    result = SendMessageInternal(service, "me", message1)
    return result

def SendMessageInternal(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print 'Message Id: %s' % message['id']
        return message
    except errors.HttpError, error:
        print 'An error occurred: %s' % error
        return "Error"
    return "OK"

def CreateMessage(sender, to, subject, msgPlain):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['Bcc'] = to
    msg.attach(MIMEText(msgPlain, 'plain'))
    return {'raw': base64.urlsafe_b64encode(msg.as_string())}

def main():
    to = "bagustyo92@gmail.com, muhammad.irfan.reza@gmail.com, mukmiin11@gmail.com, yandracharlostulus@gmail.com"
    sender = "wikabangunangedung@gmail.com"
    subject = "Testing"
    msgPlain = "You have comment on 'Wika Gedung Dashboard App'\nClick here to open : http://www.wikagedung.co.id/launch\n\nRegards, Wika Gedung"
    SendMessage(sender, to, subject, msgPlain)

if __name__ == '__main__':
    main()