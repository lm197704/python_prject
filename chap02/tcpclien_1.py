import socket

target_ip='127.0.0.1'
target_port=9998

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((target_ip,target_port))

client.send(b'hello')
res=client.recv(4096)

print(res.decode('utf-8'))