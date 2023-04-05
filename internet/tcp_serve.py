import socket


def main():
    #买一个电话，创建套接字
    tcp_serve_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #插卡，绑定本地信息
    tcp_serve_socket.bind(("",8959))
    #设定为响铃模式
    tcp_serve_socket.listen(128)
    #等电话来
    new_clien_socket , client_addr=tcp_serve_socket.accept()

    #用新的套接字接受信息
    recv_data = new_clien_socket.recv(1024)
    print(recv_data.decode("gbk"))

    #发送确认信息
    new_clien_socket.send("收到".encode("gbk"))
    new_clien_socket.close()
    tcp_serve_socket.close()


if __name__ =="__main__":
    main()