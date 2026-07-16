import socket
import time
import datetime



IP_SERVER = socket.gethostbyname(socket.gethostname())
# IP_SERVER = "localhost"  # Use localhost for testing purposes
PORT = 9999
ADDRESS = (IP_SERVER, PORT)

def recvUser(): 

    userReq = int(connection.recv(1024).decode("utf-8"))

    if userReq == 1:
        answer = time.ctime()
        connection.send(f"The current time is {answer}".encode("utf-8"))
    elif userReq == 2:
        answer = datetime.datetime.now().strftime("%Y-%m-%d")
        connection.send(f"Today's date is {answer}".encode("utf-8"))

# serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind(ADDRESS)
print(f"Server is running on {IP_SERVER}:{PORT}")

serverSocket.listen(5)

lstofQuest = ["1. What time is it?", "2. What is todays date?"]

while True:
    print("Waiting for a connection...")
    connection, addr = serverSocket.accept()
    print(f"Connection from {addr} has been established!")

    connection.send(f"Welcome to the server! Hello client, ask the following questions:\n {', '.join(lstofQuest)}".encode("utf-8"))
    recvUser()

    