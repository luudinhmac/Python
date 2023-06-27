from email import message_from_bytes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import make_msgid
from imaplib import IMAP4, IMAP4_SSL, IMAP4_PORT, IMAP4_SSL_PORT
from smtplib import SMTP, SMTP_SSL, SMTP_SSL_PORT,SMTP_PORT
from subprocess import call
from textwrap import dedent
from time import sleep



__author__ ='Bertrand  Bordage'
__copyright__ = 'Copyright © 2016 Bertrand Bordage'
__license__ = 'MIT'

class AutoReplyer:
    refress_delay =5
    imap_server =None
    imap_use_ssl =False
    imap_port =IMAP4_PORT
    imap_ssl_port = IMAP4_SSL_PORT
    imap_user =None
    imap_password =None

    smtp_server =None
    smtp_use_ssl =False
    smtp_port =SMTP_PORT
    smtp_ssl_port =SMTP_SSL_PORT
    smtp_user =None
    smtp_password=None

    from_address =None
    body =None
    body_html=None

    def __init__(self):
        if self.imap_use_ssl:
            self.imap =IMAP4_SSL(self.imap_server,self.imap_ssl_port)
        else:
            self.imap=IMAP4(self.imap_server,self.imap_port)
        self.imap.login(self.imap_user,self.imap_password)
        if self.smtp_use_ssl:
            self.smtp=SMTP_SSL(self.smtp_server,self.smtp_ssl_port)
        else:
            self.smtp=SMTP(self.smtp_server,self.smtp_port)
        self.smtp.login(self.smtp_user,self.smtp_password)

def close(self):
    self.close()
    self.imap.logout()
def create_auto_reply(self, original):
    mail = MIMEMultipart('alternative')
    mail['Message-ID']=make_msgid()
    mail['References']=mail['In-Reply-To']=original['Message-ID']
    mail['Subject']='Re: ' + original['Subject']
    mail['From']=self.from_address
    mail.attach(MIMEText(dedent(self.body),'plain'))
    mail.attach(MIMEText(self.body_html),'html')
    return mail

def send_auto_reply(self, original):
    self.smtp.sendmail(
        self.from_address, [original['From']],
        self.create_auto_reply(original).as_bytes()
    )
    log= 'Replied to "%s" for the mail "%s"' % (original['From'],original['Subject'])
    print(log)
    try:
        call(['notify-send',log])
    except FileNotFoundError:
        pass

def reply(self,mail_number):
    self.imap.select(readonly=True)
    _, data =self.imap.fetch(mail_number,'(RFC822')
    self.imap.close()
    self.send_auto_reply(message_from_bytes(data[0][1]))
    self.imap.select(readonly=False)
    self.imap.store(mail_number, '+FLAGS', '\\Answered')
    self.imap.close()

def check_mails(self):
    self.imap.select(readonly=False)
    _,data =self.imap.search(None,'(UNSEEN UNANSEWERD)')
    self.imap.close()
    for mail_number in data[0].split():
        self.reply(mail_number)
def run(self):
    try:
        while True:
            self.check_mails()
            sleep(self.refresh_delay)
    finally:
        self.close()
