import socket

s = socket.socket(socket.AF_INET , socket.SOCK.STREAM)
s.connect((socket.gethostname(), 12345))

msg = s.recv(1024)
print(msg.decode("utf-8"))
