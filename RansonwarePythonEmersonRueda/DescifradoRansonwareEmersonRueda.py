#Descifrado Ransonware Emerson Rueda

from cryptography.fernet import Fernet
import os

#############################################################################


# Cargar la llave generada
def cargar_key():
    return open('key_Emer.key', 'rb').read()


# Descifrar
def descifrar(items, key):
    f = Fernet(key)
    for item in items:
        # Leo el archivo cifrado
        with open(item, 'rb') as file:
            encrypted_data = file.read()

        decrypted_data = f.decrypt(encrypted_data)

        # Escribo el archivo descifrado
        with open(item, 'wb') as file:
            file.write(decrypted_data)

        os.rename(item, item)

if __name__=='__main__':
    path_to_decrypt = 'D:/CifradoDescrifadoDatos'
    items=os.listdir(path_to_decrypt)
    full_path = [path_to_decrypt + '\\' + item for item in items]

    #Cargar la llave
    key=cargar_key()
    descifrar(full_path, key)

    file_path='D:/CifradoDescrifadoDatos/Descifrado.txt'


    with open(file_path, 'w') as file:
        file.write('Se�or Emerson, los archivos fueron descifrados exitosamente')
