import socket
import sys
from thread import *

hi = "<html> <body> hello </body> </html>"


HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

s.listen(10)
print 'Socket now listening'

#Function for handling connections
def clientthread(conn):
    a = 8
    #Sending message to connected client
    #conn.send(hi)
    # conn.send('Welcome to the server. Receving Data...\n') #send only takes string

    #infinite loop so that function do not terminate and thread do not end.
    while a > 5:

        #Receiving from client
        data = conn.recv(86066)
        reply = 'Message Received at the server!\n'
        print data
        a = a - 1
        if not data:
           break

        #conn.sendall(hi)

    conn.close()

#now keep talking with the client
while 1:
    #wait to accept a connection
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    cfile = conn.makefile('rw', 0)
    line = cfile.readline().strip()
    cfile.write('HTTP/1.0 200 OK\n\n')
    cfile.write('<html><head><title>Welcome %s!</title></head>' %(str(conn)))
    cfile.write('<body><h1>Follow the link...</h1>')
    cfile.write('All the server needs to do is ')
    cfile.write('to deliver the text to the socket. ')
    cfile.write('It delivers the HTML code for a link, ')
    cfile.write('and the web browser converts it. <br><br><br><br>')
    cfile.write('<font size="7"><center> <a href="http://python.about.com/index.html">Click me!</a> </center></font>')
    cfile.write('<br><br>The wording of your request was: "%s"' %(line))
    cfile.write('</body></html>')
    #start new thread
    #start_new_thread(clientthread ,(conn,))
    cfile.close()
    conn.close()

s.close()
