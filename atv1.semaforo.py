import threading
import time
import random

semaforo = threading.Semaphore(3) #Define a quantidade de threading

def atendimento():
    semaforo.acquire()
    print(threading.currentThread().getName())
    time.sleep(random.randint(3,10))
    semaforo.release()

def lista_():
    return list(range(1,31))
    


if __name__=="__main__":
    t1 = threading.Thread(target=atendimento)
    t2 = threading.Thread(target=atendimento)
    t3 = threading.Thread(target=atendimento)
    
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
 
print(lista_())

