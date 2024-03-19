import smtplib, ssl 
from email.message import EmailMessage 
import imghdr
smtp_server = "smtp.gmail.com"
port = 587
sender_email = "s1ncepr3m@gmail.com"
password=input("Kirjuta oma salasõna ja vajuta enter: ")
context = ssl.create_default_context()
receiver_email=input("Sisesta email: ")
message=input("Sisesta sõnumi tekst: ")
teema=input("Sisesta teema: ")
msg = EmailMessage()
msg.set_content(message)
msg['Subject']=teema
msg['From']="Valera Ashurov"
msg['To']=receiver_email
with open("maxresdefault.jpg",'rb') as fpilt:
    pilt=fpilt.read()
msg.add_attachment(pilt,maintype='image',subtype='jpg')
try: 
    server = smtplib.SMTP(smtp_server,port)
    server.starttls(context=context)
    server.login(sender_email,password)
    server.send_message(msg)
    print("Kiri on saatnud")
except Exception as e:
    print(e)
finally:
    server.quit()