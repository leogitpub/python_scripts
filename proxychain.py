import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('183.32.22.22', 8080))
    ''' s.connect(('61.73.22.22' , 8080))'''
    request = b"CONNECT 146.23.22.22:80 HTTP/1.1\n\n"
    s.send(request)
    print('hi' + s.recv(4096).decode())
    request = b"GET google.com HTTP/1.1\n\n"
    s.send(request)
    print(s.recv(4096).decode())

main()
