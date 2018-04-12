#coding:utf-8
import socket

ip=("127.0.0.1",8100)

node=socket.create_connection(ip)
print("链接服务器成功")
while True:
    data=input("请给服务端发送消息")
    node.sendall(bytes(data,"utf-8"))
    if data=="Bye":
        print("已经与服务端切断联系")
        break
    print("已经成功给服务端发送消息"+data)
    print("等待服务端返回消息")
    rec_data=node.recv(1024)
    print("服务端返回的信息:"+str(rec_data,"utf-8"))