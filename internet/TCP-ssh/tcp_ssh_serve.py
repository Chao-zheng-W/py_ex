#tcp协议 ssh实现
import socket
import subprocess
serve_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serve_socket.bind(("127.0.0.1",8081))
serve_socket.listen()

#接受
conn,client_addr = serve_socket.accept()
while True:
    #收命令
    cmd = conn.recv(1024)
    print(cmd)
    #计算结果
    obj = subprocess.Popen(cmd.decode("utf-8") , shell=True,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
    stdout = obj.stdout.read()
    stderr = obj.stderr.read()

    #发结果
    conn.send(stdout+stderr)

conn.close()
serve_socket.close()