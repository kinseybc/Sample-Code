#This is for setting up a server using Python

import socket
import sys

def main():
    host=socket.gethostname()

    #this sets the port number and can be changed
    port=1337

    try:
        s=socket.socket()
        #s.setscoketop()
        #bind takes a tuple as parameter of the hostname and port number
        s.bind((host,port))

    except socket.error,msg:
        s.close()
        print msg
        sys.exit(1)

    s.listen(1)
    #accept 1 connection

    while True:
        print "Server waiter for client on %s:%d" %(host,port)

        conn, addr=s.accept()

        print 'connection from', addr
