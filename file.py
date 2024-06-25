import socket
import threading
import hashlib
import base64
from cryptography.fernet import Fernet

# Server-side code
class Server:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('localhost', 12345))
        self.server_socket.listen(5)
        self.secret_key = Fernet.generate_key()
        print("Server started. Waiting for connections...")
        print("Secret key:", self.secret_key.decode())

    def handle_client(self, client_socket):
        client_public_key = client_socket.recv(1024)
        print("Received client's public key:", client_public_key.decode())
        shared_secret_key = hashlib.sha256(client_public_key + self.secret_key).digest()
        print("Shared secret key:", shared_secret_key.hex())
        fernet = Fernet(base64.urlsafe_b64encode(shared_secret_key))
        while True:
            encrypted_message = client_socket.recv(1024)
            print("Received encrypted message:", encrypted_message.decode())
            decrypted_message = fernet.decrypt(encrypted_message)
            print("Decrypted message:", decrypted_message.decode())
            response = "Server received your message!"
            encrypted_response = fernet.encrypt(response.encode())
            client_socket.sendall(encrypted_response)

    def start(self):
        while True:
            client_socket, address = self.server_socket.accept()
            print("Connected by", address)
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

# Client-side code
class Client:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 12345))
        print("Connected to the server!")
        self.client_public_key = "Client's public key".encode()
        print("Client's public key:", self.client_public_key.decode())
        self.client_socket.sendall(self.client_public_key)
        self.shared_secret_key = self.client_socket.recv(1024)
        print("Received shared secret key:", self.shared_secret_key.decode())
        self.fernet = Fernet(base64.urlsafe_b64encode(self.shared_secret_key))

    def send_message(self):
        while True:
            message = input("Enter a message: ")
            encrypted_message = self.fernet.encrypt(message.encode())
            print("Encrypted message:", encrypted_message.decode())
            self.client_socket.sendall(encrypted_message)
            encrypted_response = self.client_socket.recv(1024)
            print("Received encrypted response:", encrypted_response.decode())
            decrypted_response = self.fernet.decrypt(encrypted_response)
            print("Decrypted response:", decrypted_response.decode())

    def start(self):
        message_thread = threading.Thread(target=self.send_message)
        message_thread.start()

# Run the server and client
server = Server()
server_thread = threading.Thread(target=server.start)
server_thread.start()

client = Client()
client.start()