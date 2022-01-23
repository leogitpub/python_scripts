import socket
import sys
def main():
    if(len(sys.argv) < 4) :
        print 'Usage : python client.py hostname'
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    proxy = sys.argv[3]
    act = sys.argv[4]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    ''' s.connect(('61.7' , 8080))'''
    request = b"CONNECT " + proxy +  " HTTP/1.1\r\n\r\n"
    print(request)
    s.send(request)
    req = b"GET " + act + " HTTP/1.1\r\n\n\r"
    print(req)
    s.send(req)
    '''print('hi' + s.recv(4096).decode())'''
    print(s.recv(8192).decode())

main()
'''python proxy.py 138.123.123.133 3128 http://whatismyip.host/'''

