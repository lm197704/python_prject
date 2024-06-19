import socket

target_ip='www.baidu.com'
target_port=80

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((target_ip,target_port))

client.send(b'GET / HTTP/1.1\r\nHost:baidu.com\r\n\r\n')
res=client.recv(4096)

print(res.decode('utf-8'))