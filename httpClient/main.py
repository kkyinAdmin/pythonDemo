# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import http.client
from urllib import request, parse


def httpPost(url, path, data, header):
    conn = http.client.HTTPConnection(url)
    # 这里报错待调试
    conn.request("POST", path, data, header)
    r1 = conn.getresponse()
    # print(r1)
    print(r1.status, r1.reason)

    recvData = r1.read()
    print(recvData)  #
    conn.close()
    return recvData


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = "http://127.0.0.1:5000"
    data = {
        'test',
    }
    path = "\\";
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    recvData = httpPost(url, path, data, headers)
    # print("收到返回"+recvData)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
