#tcp协议 ssh实现
import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1",8081))

while True:
    #发命令
    cmd = input(">>--")
    client_socket.send(cmd.encode("utf-8"))

    #收结果
    data = client_socket.recv(1024)
    print(data.decode("gbk"))
client_socket.close()