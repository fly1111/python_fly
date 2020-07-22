import socket
import random
sk = socket.socket()

ip_port = ('127.0.0.1',8888)

sk.bind(ip_port)
sk.listen(5)
while True:
    #提示信息
    print('正在进行等待接受数据')
    #接受数据
    conn,address = sk.accept()
    #定义信息
    msg = '连接成功'
    #返回信息网络协议发送及接收都是byte类型
    #str时需要转码
    conn.send(msg.encode())
    #不断接受客户发送的消息
    while True:
        data = conn.recv(1024)
        print(data.decode())
        if data == b'exit':
            break
        conn.send(data)
        #发送随机数
        conn.send(str(random.randint(1,1000)).encode())
    conn.close()


