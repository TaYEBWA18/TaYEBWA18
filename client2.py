import socket
import threading

PORT = 65000
SERVER = "192.168.100.103"
ADDR = (SERVER, PORT)
FORMAT = "ascii"
DISCONNECTED_MESSAGE = "!DISCONNECTED"


username = input("Enter your username:")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def receiveMessage():
    while True:
        try:
            message = client.recv(1024).decode(FORMAT)
            if message == "USERNAME!":
                client.send(username.encode(FORMAT))
            else:
                print(message)
        except:
            print("An error occurred")
            client.close()
            break


def sendMessage():
    connected = True
    while connected:
        msg = input("")
        message = f"{username}:{msg}"
        client.send(message.encode(FORMAT))
        if msg == DISCONNECTED_MESSAGE:
            connected = False
    client.close()


receiveThread = threading.Thread(target=receiveMessage)
sendThread = threading.Thread(target=sendMessage)
receiveThread.start()
sendThread.start()
