# coding:utf-8

import socket

hub = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
ip = ("127.0.0.1", 8100)
hub.bind(ip)
hub.listen(5)
import subprocess
while True:
    print(u"服务器端开始监听")
    conn, addr = hub.accept()
    print("来自ip%s的问候" % addr[0])
    while True:
        print("等待客户端消息....")
        try:
            data = conn.recv(1024)
        except:
            print("该客户端%s已经切断联系")
            break
        else:
            print("客户端发送了命令:" + str(data, "utf-8"))
            print("开始执行命令")
            cmd=str(data, "utf-8")
            if cmd=="Bye":
                print("客户端已经切断了联系__ip:%s"%addr[0])
                break
            data=subprocess.check_output(cmd,shell=True)
            conn.sendall(data)
            print("向客户端发送执行命令结果:\t"+str(data,"utf-8"))




