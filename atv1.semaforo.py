'''
Escreva um programa em Python, que simule a fila de atendimento de um banco. O banco possui 3 caixas. O tempo de atendimento de cada cliente deve ser um tempo aleatório entre 3 a 10 segundos. Suponha que a fila tenha um tamanho fixo com 30 clientes em espera. Utilize um semáforo para fazer o gerenciamento dos recursos compartilhados (caixas) entre os clientes (threads). 
'''

import threading
import time
import random

semaforo = threading.Semaphore(3) #Define a quantidade de threading

def atendimento(id):
    semaforo.acquire()
    print("Cliente {}".format(id) + " em atendimento")
    time.sleep(random.randint(3,10))
    print("Finalizando...{}".format(id))

    semaforo.release()
    

if __name__=="__main__":

    threadsaqui =  []

    for i in range(1, 31):
        theread = threading.Thread(target=atendimento, args=(i, ))
        threadsaqui.append(theread)


    for thread in threadsaqui:
        thread.start()

    for thread in threadsaqui:
        thread.join()

