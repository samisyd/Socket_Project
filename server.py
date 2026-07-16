import socket
import signal
import sys
import time
import datetime

# IP_SERVER = socket.gethostbyname(socket.gethostname())
IP_SERVER = "localhost"
PORT = 9999
ADDRESS = (IP_SERVER, PORT)

class GracefulServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # SO_REUSEADDR prevents "Address already in use" errors when restarting quickly
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        self.is_running = True

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        # Set a timeout on accept() so the loop can periodically check if self.is_running is False
        self.server_socket.settimeout(1.0)
        
        print(f"[SERVER STARTED] Listening on {self.host}:{self.port}")
        print("Press Ctrl+C to stop the server gracefully.\n")

        try:
            while self.is_running:
                try:
                    connection, addr = self.server_socket.accept()
                    self.handle_client(connection, addr)
                except socket.timeout:
                    # Timeout reached without connection; loop continues and checks self.is_running
                    continue
        except KeyboardInterrupt:
            print("\n[SHUTDOWN SIGNAL] KeyboardInterrupt received.")
        finally:
            self.shutdown()

    def handle_client(self, connection, addr):
        """Handles single client interaction safely."""
        print(f"[NEW CONNECTION] {addr} connected.")
        try:
            connection.send("Welcome! Available options: 1 (Time), 2 (Date)".encode("utf-8"))
            while self.is_running:
                data = connection.recv(1024).decode("utf-8")
                if not data:
                    print(f"[DISCONNECT] Client {addr} disconnected.")
                    break
                
                req = int(data)
                if req == 1:
                    response = f"Current time: {time.ctime()}"
                elif req == 2:
                    response = f"Today's date: {datetime.datetime.now().strftime('%Y-%m-%d')}"
                else:
                    response = "Invalid option."
                
                connection.send(response.encode("utf-8"))
        except (ValueError, ConnectionResetError):
            pass
        finally:
            connection.close()

    def shutdown(self):
        """Clean up resources on server exit."""
        print("[SHUTTING DOWN] Closing server socket and releasing ports...")
        self.is_running = False
        self.server_socket.close()
        print("[OFFLINE] Server gracefully stopped.")

if __name__ == "__main__":
    server = GracefulServer(IP_SERVER, PORT)
    server.start()