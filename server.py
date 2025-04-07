import socket
import threading
from crypto_utils import generate_key, encrypt_message, decrypt_message, generate_session_id

class ChatServer:
    def __init__(self, host='0.0.0.0', port=5000):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = {}
        self.encryption_key = generate_key()
        
    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server in ascolto su {self.host}:{self.port}")
        
        while True:
            client_socket, address = self.server_socket.accept()
            session_id = generate_session_id()
            self.clients[client_socket] = (address, session_id)
            
            client_socket.send(self.encryption_key)
            
            client_thread = threading.Thread(
                target=self.handle_client,
                args=(client_socket, address, session_id)
            )
            client_thread.start()
            
    def handle_client(self, client_socket, address, session_id):
        try:
            while True:
                encrypted_message = client_socket.recv(4096).decode()
                if not encrypted_message:
                    break
                    
                message = decrypt_message(encrypted_message, self.encryption_key)
                self.broadcast_message(message, client_socket)
                
        except Exception as e:
            print(f"Errore nella gestione del client {address}: {e}")
        finally:
            self.remove_client(client_socket)
            
    def broadcast_message(self, message, sender_socket):
        for client in self.clients:
            if client != sender_socket:
                try:
                    encrypted_message = encrypt_message(message, self.encryption_key)
                    client.send(encrypted_message.encode())
                except:
                    self.remove_client(client)
                    
    def remove_client(self, client_socket):
        if client_socket in self.clients:
            del self.clients[client_socket]
            client_socket.close()

if __name__ == "__main__":
    server = ChatServer()
    server.start()