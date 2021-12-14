# 这是一个示例 Python 脚本。
# socket客户端 输入IP 端口号与服务端建立连接

import socket

from pip._vendor.distlib.compat import raw_input


def socketConnect(socketIP, socketPORT):
    try:
        skClient.connect((socketIP, int(socketPORT)))  # 尝试连接服务器
    except:
        print("连接异常！")
    else:
        print("连接成功！")


def socketSend(sendMsg):
    try:
        print('DAT--->：' + sendMsg)
        skClient.sendall(sendMsg.encode())
        # ret = skClient.recv(1024)  # 对话(发送/接收)
        # print(ret.decode())
    except:
        print("发送异常！")


def socketRecv():
    try:
        recvMsg = skClient.recv(1024)  # 对话(发送/接收)
        print('DAT<---：' + recvMsg.decode())
        return recvMsg.decode()
    except:
        print("接收异常！")
        return ""


def socketClose():
    skClient.close()  # 关闭客户套接字


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    global skClient
    skClient = socket.socket()  # 创建客户套接字
    # print("未进行socket连接，请先进行连接！！！")
    # socketIP = input('请输入IP：')
    # socketPORT = input('请输入端口：')
    # socketConnect(socketIP, socketPORT)
    recvMsg = ""
    while 1:
        if recvMsg == "":
            print("未进行socket连接，请先进行连接！！！")
            socketIP = input('请输入IP：')
            socketPORT = input('请输入端口：')
            socketConnect(socketIP, socketPORT)
        sendMsg = raw_input('请输入要发送的报文：')
        socketSend(sendMsg)
        recvMsg = socketRecv()
