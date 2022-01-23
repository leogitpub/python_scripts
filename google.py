import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "www.google.com"
port = 80
server_ip = socket.gethostbyname(server)
print(str(server_ip))
