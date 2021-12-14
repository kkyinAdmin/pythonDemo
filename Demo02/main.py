# 这是一个示例 Python 脚本。
# socket客户端 输入IP 端口号与服务端建立连接

import socket

from pip._vendor.distlib.compat import raw_input


def socketConnect(argvSocketIP, argvSocketPORT):
    try:
        skClient.connect((argvSocketIP, int(argvSocketPORT)))  # 尝试连接服务器
    except:
        print("连接异常！")
        return False
    else:
        print("连接成功！")
        return True


def socketSend(argvSendMsg):
    try:
        print('DAT--->：' + argvSendMsg)
        skClient.sendall(argvSendMsg.encode())
        # ret = skClient.recv(1024)  # 对话(发送/接收)
        # print(ret.decode())
    except:
        print("发送异常！")


def socketRecv():
    try:
        tmpRecvMsg = skClient.recv(1024)  # 对话(发送/接收)
        print('DAT<---：' + tmpRecvMsg.decode())
        if tmpRecvMsg.decode() == "":
            socketClose()
        return tmpRecvMsg.decode()
    except:
        print("接收异常！")
        socketClose()
        return ""


def socketClose():
    skClient.close()  # 关闭客户套接字


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    global skClient
    # print("未进行socket连接，请先进行连接！！！")
    # socketIP = input('请输入IP：')
    # socketPORT = input('请输入端口：')
    # socketConnect(socketIP, socketPORT)
    recvMsg = ""
    while 1:
        if recvMsg == "":  # 初始提交和异常接受都为空
            print("未进行socket连接，请先进行连接！！！")
            socketIP = input('请输入IP：')
            socketPORT = input('请输入端口：')
            skClient = socket.socket()  # 创建客户套接字
            ret = socketConnect(socketIP, socketPORT)
            if not ret:
                continue
        sendMsg = raw_input('请输入要发送的报文：')  # input
        socketSend(sendMsg)
        recvMsg = socketRecv()
