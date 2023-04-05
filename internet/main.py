import socket

def main():
     udp_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建套接字
     udp_socket.bind(("",7879))  # 用元组表示ip和port
     udp_socket.sendto("你好呀".encode("UTF-8"),("59.79.240.203", 8081))
     rec_data = udp_socket.recvfrom(1024)
     rec_comment = rec_data[0].decode("UTF-8")
     rec_addr = rec_data[1]
     print(rec_comment)
     udp_socket.close()

if __name__ == "__main__":
    main()