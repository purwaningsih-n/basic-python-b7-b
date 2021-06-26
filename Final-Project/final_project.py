## Program untuk mengirim email. Alamat email penerima disimpan pada file txt
## referensi: 
## https://code.tutsplus.com/id/tutorials/sending-emails-in-python-with-smtp--cms-29975
## https://python.web.id/posts/detail/mengirim-email-gmail-via-python/
## https://ichi.pro/id/cara-mengirim-email-dengan-lampiran-dengan-python-188994555473139

## Membaca daftar penerima email dari file
with open('receiver_list.txt', 'r') as file:
    penerima = file.read().replace('\n', ',')

#-------------------------------------------------
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

import smtplib

# create message object instance
msg = MIMEMultipart()


# setup the parameters of the message
pengirim = "apelsemangka9999@gmail.com"
msg ['Subject'] = 'Mengirim email melalui program Python'
msg ['From'] = pengirim
msg ['To'] = penerima

password = input("password email pengirim = ")

# attach text to message body
filename = "isi_email.txt"
msg.attach(MIMEText(open(filename).read()))


# attach image to message body
with open('clutch.jpg', 'rb') as fp:
    img = MIMEImage(fp.read())
    img.add_header('Content-Disposition', 'attachment', filename="clutch.jpg")
    msg.attach(img)


# create server
server = smtplib.SMTP('smtp.gmail.com: 587')

server.starttls()

# Login Credentials for sending the mail
server.login(pengirim, password)


# send the message via the server.
server.sendmail(msg['From'], msg["To"].split(","), msg.as_string())

server.quit()

print ("berhasil mengirim email") 
