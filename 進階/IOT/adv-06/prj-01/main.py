import socket


host = "localhost"
port = 5438
sever_socket = socket.socket()
sever_socket.bind((host, port))
sever_socket.listen(5)
print("sever:{}port:{}start".format(host, port))  #
client, addr = sever_socket.accept()
print("client address:{},port:{}".format(addr[0], addr[1]))

while True:
    msg = client.recv(128).decode("utf8")
    print("Receive Message")
    reply = ""

    if msg == "Hi":
        reply = "Hello!"
        client.send(reply.encode("utf8"))
    elif msg == "Bye":
        client.send(b"quit")
        break
    else:
        reply = "What!"
        client.send(reply.encode("utf8"))
client.close()
sever_socket.close()
