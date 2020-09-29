import socket
import threading

PORT = 5050
#SERVER = "192.168.43.96"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print("[NEW CONNECTION] {addr} connected.")

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print("[ACTIVE CONNECTION] {threading.activeCount() - 1}")

print("[STARTING] Server is starting...")
start()