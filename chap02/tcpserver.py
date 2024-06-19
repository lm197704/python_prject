import socket
import threading


def main(args=None):
    
    target_ip='127.0.0.1'
    target_port=9998

    server=socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server.bind((target_ip,target_port))
    server.listen(5)

    while True:
        client,addr=server.accept()
        print(f'client comes from {addr[0]}:{addr[1]}')
        thread=threading.Thread(target=client_handler,args=(client,))
        thread.run()


def client_handler(client_socket):
    
    res=client_socket.recv(4096).decode('utf-8')
    print(f'the client is saying {res}')
    client_socket.send(b'i am server')
    pass


if __name__=="__main__":
    main()