import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# This is a static salt used to stretch manual passwords.
# Keep this consistent, or keys generated from passwords won't match!
MY_SALT = b'q\xe3Q5\x8c\x19~\x17\xcb\x88\xc6A\xb8j\xb4\x85'


def generate_auto_key() -> bytes:
    """Generates and returns a completely random Fernet key."""
    return Fernet.generate_key()


def generate_password_key(password: str) -> bytes:
    """Turns a plain text password into a secure Fernet key."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=MY_SALT,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))


def encrypt_data(data: bytes, key: bytes) -> bytes:
    """Encrypts raw bytes using the provided key and returns encrypted bytes."""
    fernet = Fernet(key)
    return fernet.encrypt(data)


def decrypt_data(encrypted_data: bytes, key: bytes) -> bytes:
    """Decrypts encrypted bytes using the provided key and returns original bytes."""
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data)
