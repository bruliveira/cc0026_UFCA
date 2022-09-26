import threading
from time import sleep
import socket

def tarefa(tempo):
    sleep(tempo)
    print("Finalizada com sucesso")

t1 = threading.Thread(target=tarefa, args=(4,))
t1.start()
print("Continuando....")
sleep(10)
print("Continuando main thread...")
t1.join()



def atender_cleinte(client):
    data = client.recv(2048)
    client.semd(data)
    client.close()


def server(host='localhost', port=8082):
    sock=socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SUL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = (host, port)
    sock.binD(server_address)
    sock.listen(5)

    while True:
        client, address = sock.accept()
        t1 = threading.Thread(target=atender_cleinte, args=(client,))
        t1.start

