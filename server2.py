import socket
import threading
import time

HOST = socket.gethostbyname(socket.gethostname())
PORT = 65000
ADDR = (HOST, PORT)
FORMAT = "ascii"
DISCONNECTED_MESSAGE = "!DISCONNECTED"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
clients = []
usernames = []


def bootServer():
    print("[BOOTING]")
    time.sleep(2)
    print("[BOOTING] ....")
    time.sleep(1)
    print("[BOOTING] .......")
    time.sleep(1)
    print("[BOOTING] ..............")
    time.sleep(1)
    print("[BOOTING] ....................")
    time.sleep(1)
    print("[BOOTING] ............................")
    time.sleep(1)
    print("[BOOTING] ..........................................")
    time.sleep(1)
    print("[STARTING] Server is starting.............................")
    time.sleep(3)


def broadcastMessage(message):
    for client in clients:
        client.send(message)

#TO HANDLE CLIENTS
def handleClient(client):
    while True:
        try:
            message = client.recv(1024)
            broadcastMessage(message)

        except:
            index = clients.index(client)
            clients.remove(client)
            clients.close()
            username = usernames[index]
            broadcastMessage(f"{username} has left the chat")
            usernames.remove(username)


def start():
    users = 1
    server.listen()
    print(f"[LOG 0] [SERVER STARTED] Server is listening in on {HOST}:{PORT}")
    while True:
        client, address = server.accept()
        print(f"[ LOG {users} ] [NEW CONNECTION] {address} connected")

        client.send("USERNAME!".encode(FORMAT))
        username = client.recv(1024).decode(FORMAT)
        usernames.append(username)
        print(f"[LOG {users}.1] [NEW CONNECTION] Connected as {username}")
        clients.append(client)
        broadcastMessage(f"\n{username} joined the chat".encode(FORMAT))
        client.send("\nConnected to the server".encode(FORMAT))

        thread = threading.Thread(target=handleClient, args=(client,))
        thread.start()
        users = threading.active_count()


bootServer()
start()
