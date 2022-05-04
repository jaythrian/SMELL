import socket
from time import sleep

f = open("detected.txt", "w+")

HOST = "192.168.0.158" # Standard loopback interface address (localhost)
PORT = 65432 # Port to listen on (non-privliged ports are > 1023)

# boilerplate socket code
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SQL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024) # receives data from client
            conn.sendall(data)
            f.write(data) # write data to file
            sleep(3)
