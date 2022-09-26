import threading
from time import sleep

def tarefa(tempo):
    sleep(tempo)
    print("Finalizada com sucesso")

t1 = threading.Thread(target=tarefa, args=(4,))
t1.start()
print("Continuando....")
sleep(10)
print("Continuando main thread...")
t1.join()
