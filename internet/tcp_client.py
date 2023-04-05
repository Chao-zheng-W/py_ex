import socket

def main():
    #创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect(("59.79.240.203",8080))

    #发送数据
    tcp_socket.send(b"haha")

    #关闭套接字
    tcp_socket.close()

if __name__  =="__main__":
    main()