#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket  # 导入 socket 模块

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建 socket 对象
host = "127.0.0.1"  # 获取本地主机名
port = 10086  # 设置端口
s.bind((host, port))  # 绑定端口

s.listen(5)  # 等待客户端连接
while True:
    c, addr = s.accept()  # 建立客户端连接

    print(addr)
    message = c.recv(1024).decode()
    print(":" + message)
    c.send(("已经收到您的消息！"+message).encode())
    print(len(message))
    print(len(message.encode()))
    c.close()  # 关闭连接