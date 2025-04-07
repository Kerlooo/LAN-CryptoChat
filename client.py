import socket
import threading
from crypto_utils import encrypt_message, decrypt_message

class ChatClient:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.encryption_key = None
        
    def connect(self):
        try:
            self.client_socket.connect((self.host, self.port))
            self.encryption_key = self.client_socket.recv(4096)
            print(f"Connesso al server {self.host}:{self.port}")
            return True
        except Exception as e:
            print(f"Errore di connessione: {e}")
            return False
            
    def start(self):
        if not self.connect():
            return
            
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.daemon = True
        receive_thread.start()
        
        self.send_messages()
        
    def receive_messages(self):
        while True:
            try:
                encrypted_message = self.client_socket.recv(4096).decode()
                if not encrypted_message:
                    break
                    
                message = decrypt_message(encrypted_message, self.encryption_key)
                print(f"\nMessaggio ricevuto: {message}")
                
            except Exception as e:
                print(f"Errore nella ricezione: {e}")
                break
                
        self.disconnect()
        
    def send_messages(self):
        while True:
            try:
                message = input("> ")
                if message.lower() == 'quit':
                    break
                    
                encrypted_message = encrypt_message(message, self.encryption_key)
                self.client_socket.send(encrypted_message.encode())
                
            except Exception as e:
                print(f"Errore nell'invio: {e}")
                break
                
        self.disconnect()
        
    def disconnect(self):
        try:
            self.client_socket.close()
        except:
            pass
        print("\nDisconnesso dal server")

if __name__ == "__main__":
    client = ChatClient()
    client.start()