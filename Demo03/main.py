# 这是一个示例 Python 脚本。
# socket服务端 绑定输入的端口

import socket

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    global skServer
    recvMsg = ''
    while 1:
        if recvMsg == '':
            socketPORT = input('请输入绑定端口：')
            try:
                skServer = socket.socket()  # 创建客户套接字
                skServer.bind(('127.0.0.1', int(socketPORT)))  # 把地址绑定到套接字
                skServer.listen()  # 监听链接
            except:
                print('绑定异常！')
                continue
            print("端口绑定成功，等待客户端连接")
            conn, addr = skServer.accept()  # 接受客户端链接
            print("客户端连接成功")
        try:
            tmpRecvMsg = conn.recv(1024)  # 接收客户端信息
        except:
            print('获取客户端报文异常！')
            conn.close()  # 关闭客户端套接字
            skServer.close()  # 关闭服务器套接字(可选)  代码这里直接关闭服务器套接字重新绑定端口
            recvMsg = ''
            continue
        recvMsg = tmpRecvMsg.decode()  # byte解码 如b'hi'转为'hi'
        print('<---'+recvMsg)
        sendMsg = "hi"
        conn.send(sendMsg.encode())
        print('--->' + sendMsg)
