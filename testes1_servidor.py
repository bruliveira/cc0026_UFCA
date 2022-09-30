import socket 
host = 'localhost' 
port = 8082 
addr = (host, port) 
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
serv_socket.bind(addr) 
serv_socket.listen(5)
 
print ('aguardando conexao') 
con, cliente = serv_socket.accept() 
print ('conectado' )
print ("aguardando mensagem")
recebe = con.recv(1024) 

#print ("mensagem recebida: ", recebe = serv_socket.close())

print ("Dados: %s" %recebe.decode())

con.send(recebe)
con.close()
