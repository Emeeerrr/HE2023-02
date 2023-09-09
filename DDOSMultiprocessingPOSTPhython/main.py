
#main:

import json
import logging
import time
import multiprocessing
import requests

################################################################################################

page:str="http://127.0.0.1:8090/aurenticarusuario"

POST_data={'usuario':'Emerson',
           'clave:':'EmersonRueda123'
           }

payload = json.dumps(POST_data)

headers = {'accept': 'application/json',
           'Content-Type': 'application/json'}

################################################################################################

def multiprocessing_func():
    try:
        response = requests.request("POST", page, headers=headers, data=payload)
        if response.status_code == 200:
            print("Solicitud HTTP POST Exitosa", response.text)
    except Exception as e:
            print("Solicitud HTTP POST Fallida")

def demon(page, i):
    name = multiprocessing.current_process().name
    print(name, 'Inicio')
    multiprocessing_func()
    print(name, 'Fin')


################################################################################################

if __name__ == '__main__':
    multiprocessing_func()
    starttime = time.time()
    processes = []
    while True:
        i = 10
        p = multiprocessing.Process(target=demon, args=(page, i))
        processes.append(p)
        p.start()
        p.join()


