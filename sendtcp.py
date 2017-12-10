
import socket

HOST = ''
PORT = 50000

listen_s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listen_s.setsocketopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
listen_s.bind((HOST,PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s..." %PORT
while True:
	client_connection,client_addr=listen.socket.accept()
	request=client_connection.recv(1024)
	print request
	
	http_response="""\
	HTTP/1.1 200 OK
	
	HELLO, WORLD!!
	
	"""
	
client_connection.sendall(http_response)
client_conection.close()