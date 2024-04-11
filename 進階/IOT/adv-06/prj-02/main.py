import socket


client_socket = socket.socket()
client_socket.connect(("127.0.0.1", 5438))


while True:
    msg = input("input message:")
    client_socket.send(msg.encode("utf8"))
    reply = client_socket.recv(128).decode("utf8")

    if reply == "quit":
        print("Disconnected")
        client_socket.close()
        break

    print(reply)
