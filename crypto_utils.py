from cryptography.fernet import Fernet
import base64
import secrets

def generate_key():
    return Fernet.generate_key()

def encrypt_message(message: str, key: bytes) -> str:
    f = Fernet(key)
    encrypted_data = f.encrypt(message.encode())
    return base64.b64encode(encrypted_data).decode()

def decrypt_message(encrypted_message: str, key: bytes) -> str:
    f = Fernet(key)
    decrypted_data = f.decrypt(base64.b64decode(encrypted_message))
    return decrypted_data.decode()

def generate_session_id() -> str:
    return secrets.token_urlsafe(16)