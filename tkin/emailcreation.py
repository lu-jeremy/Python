import smtplib

mail = 'bluethunderleopard@gmail.com'
password = ''
subject = 'Whats up Winston'
message = 'I am sending this email from a program named python. Dont worry, Im not a stalker. Btw cant put apostrophes, messes up the message.'
receiver = 'winston.s.liu@gmail.com'
server = smtplib.SMTP('smtp.gmail.com',587)

server.ehlo()
server.starttls()
server.login(mail,password)
body = '\n'.join(['To:%s'%receiver,'From:%s'%mail,'Subject:%s'%subject,message])
server.sendmail(mail,receiver,body)
try:
    server.sendmail(mail,receiver,body)
    print('email has been sent')
except:
    print('Error')
server.quit()
