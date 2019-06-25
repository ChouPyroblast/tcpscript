import socket
HOST = '127.0.0.1'
PORT = 6666
import time
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'0')
    s.sendall(b'1')