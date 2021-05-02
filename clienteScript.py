import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 50005))
sock.sendall(str.encode('22'))
data = sock.recv(1024)

print("Connection for the First Client, making the vote to the constituent of the number 22")
print(f'Return message: {data.decode()}')
