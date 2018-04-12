#coding:utf-8

import socket

hub=socket.socket(socket.AF_INET,type=socket.SOCK_STREAM)
ip=("192.168.3.229",8100)
hub.bind(ip)
hub.listen(5)

while True:
    print(u"服务器端开始监听")
    conn,addr=hub.accept()
    print("来自ip%s的问候"%addr[0])
    while True:
        print("等待客户端消息....")
        try:

            data=conn.recv(1024)
        except:
            print("该客户端%s已经切断联系")
            break
        else:
            print("客户端说:"+str(data,"utf-8"))
            send_data=input("请输入返回给客户端的信息:")
            if send_data=="Bye":
                conn.sendall("Bye")
                break
            else:
                conn.sendall(bytes(send_data,"utf-8"))
                print("给客户端发送消息成功!")


