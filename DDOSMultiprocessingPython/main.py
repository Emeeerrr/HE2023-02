#main

#######################################################################################
import logging
import time
import multiprocessing
import requests

#######################################################################################

page: str = 'http://127.0.0.1:8090/autenticarusuario?usuario=Emer&clave=Emer123'

#######################################################################################

def multiprocessing_func(page, i):
    try:
        data = requests.get(page, verify=False)
        print('i {2} status {0}, time {1}'.format(data.status_code, data.elapsed.total_seconds(),i))
    except Exception as e:
        print('Error')

def demon(page, i):
    name = multiprocessing.current_process().name
    print(name, 'Inicio')
    multiprocessing_func(page, 1)
    print(name, 'Fin')

#######################################################################################

if __name__ == '__main__':
    starttime = time.time()
    processes = []
    while True:
        i = 10
        p = multiprocessing.Process(target=demon, args=(page, i))
        processes.append(p)
        p.start()
        p.join()