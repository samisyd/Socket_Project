import socket

# IP_SERVER = socket.gethostbyname(socket.gethostname())
IP_SERVER = "localhost"  # Use localhost for testing purposes
PORT = 9999
ADDRESS = (IP_SERVER, PORT)

# this will create a socket object for the client and AF_INET is the address family for IPv4 and SOCK_STREAM is the socket type for TCP
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect(ADDRESS)

print(f"Client connected to server at {IP_SERVER}:{PORT}")

try :
    # clientSocket.send("Hello, server!".encode("utf-8"))
    welcome_msg = clientSocket.recv(1024).decode("utf-8")
    if welcome_msg:
        print(f"Received message from server: \n {welcome_msg}")
 
    while True:
        try :
            userInput = int(input("Enter the question number (1 or 2) you want to ask (or 0 to exit): "))
        except ValueError:
            print("Invalid input. Please enter a valid question number (1 or 2) or 0 to exit.")
            continue

        if userInput == 0:
            print("Exiting the client.")
            break
        
        clientSocket.send(str(userInput).encode("utf-8"))
        msg = clientSocket.recv(1024).decode("utf-8") 
        if not msg:
            print("No response from server. Exiting.")
            break
        
        print(f"Received answer from server: {msg}")    
    
except ConnectionRefusedError:
    print(f"Could not connect to server at {IP_SERVER}:{PORT}. Is the server running?")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    clientSocket.close()
    print("Socket closed.")
    
