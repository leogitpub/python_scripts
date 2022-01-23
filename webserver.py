#!/usr/bin/env python
import random
import socket
import time
import subprocess as sp
import os

s = socket.socket()         # Create a socket object
#host = socket.getfqdn() # Get local machine name
host= ''
port = 9082
s.bind((host, port))        # Bind to the port
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print('Starting server on', host, port)
print('The Web server URL for this would be http://%s:%d/' % (host, port))

s.listen(5)                 # Now wait for client connection.

print('Entering infinite loop; hit CTRL-C to exit')
while True:
    # Establish connection with client.    
    c, (client_host, client_port) = s.accept()
    print('Got connection from', client_host, client_port)
    #c.send('Server Online\n') # This is invalid HTTP header
    c.recv(1000) # should receive request from client. (GET ....)
    c.send('HTTP/1.0 200 OK\n'.encode())
    c.send('Content-Type: text/html\n'.encode())
    c.send('\n'.encode()) # header and body should be separated by additional newline
    f= open("facebook.html","r")
    venki = f.read()
    f.close()
    c.send(venki.encode())
    #output = sp.getoutput('php -f loginPage.php')
    #print(output)
    #c.send(output.encode())
    ''' c.send(       <html>
        <body>
        <h1>Hello World</h1> this is my server!
        </body>
       </html>
    ) # Use triple-quote string.'''
    c.close()
