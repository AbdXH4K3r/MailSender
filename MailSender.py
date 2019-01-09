import os,sys
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib

def Logo():
    print("""
       [==============================================]
       [++ CODED BY ABDXSLAYER(abderrahmane_bourri) ++]
       [+++             FROM OMAGENG               +++]
       [++++  https://www.facebook.com/bourri.abd ++++]
       [+++++   http://www.github.com/ABDXH4K3r  +++++]
       [==============================================]
""")

Logo()
def mail_sender():
    mails = raw_input("Please Enter The Mail list Path : ")
    f = open(mails,'r')
    line = f.readline()
    name = raw_input("Mail Name (what victim will see): ")
    sender = raw_input("Subject : ")
    mail = 'emailt686@gmail.com'
    passwd = 'Azerty2010'
    i = 0
    choice = raw_input("You Want To :\n1. Type Text.\n2. Attach the message from an html page.\n\n > ")
    if choice == '1':
        msg = raw_input("Body (message/you can also use html): ")
        for line in f:
            i = i+1
            msgRoot = MIMEMultipart('related')
            msgRoot['Subject'] = sender
            msgRoot['From'] = name
            msgRoot['To'] = line
            msgRoot.preamble = sender
            msgAlternative = MIMEMultipart('alternative')
            msgRoot.attach(msgAlternative)
            msgText = MIMEText('Check This Now !!')
            msgAlternative.attach(msgText)
            msgText = MIMEText(msg, 'html')
            msgAlternative.attach(msgText)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(mail, passwd)
            server.sendmail(name, line, msgRoot.as_string())
            nline = line.rstrip()
            print('Email {} Has Been Sent ! (to {} ) ').format(i,nline)
            server.quit()


    if choice == '2':
        path = raw_input("Enter File Path : ")
        for line in f:
            i = i+1
            f = open(path,'r')
            msg = f.read()
            msgRoot = MIMEMultipart('related')
            msgRoot['Subject'] = sender
            msgRoot['From'] = name
            msgRoot['To'] = line
            msgRoot.preamble = sender
            msgAlternative = MIMEMultipart('alternative')
            msgRoot.attach(msgAlternative)
            msgText = MIMEText('Check This Now !!')
            msgAlternative.attach(msgText)
            msgText = MIMEText(msg, 'html')
            msgAlternative.attach(msgText)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(mail, passwd)
            server.sendmail(name, line, msgRoot.as_string())
            nline = line.rstrip()
            print('Email {} Has Been Sent ! (to {} ) ').format(i,nline)
            server.quit()
            f.close()
    f.close()

mail_sender()
x = raw_input('\nEnd...')
