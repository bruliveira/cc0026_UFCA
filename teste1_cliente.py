#!/usr/bin/python
# Coded by: Alisson Machado
# Contact: alisson.machado@responsus.com.br
#

import socket 
ip = 'localhost'
port = 8082 
addr = ((ip,port))
 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client_socket.connect(addr) 
mensagem = input("digite uma mensagem para enviar ao servidor") 

#client_socket.send(mensagem) 
client_socket.sendall(mensagem.encode('utf-8'))

print ('mensagem enviada')
client_socket.close()
