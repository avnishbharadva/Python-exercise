import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login('email','password')

server.sendmail('sender-email','reciever-email','Hello from python')

print("mail sent")
