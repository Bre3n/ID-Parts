from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password_provided = "password123"
password = password_provided.encode()

salt = b"\xe1&z\x7f\xad\xf0\xb4\xb6\xa8\xc0\xc5\xd9\xcea\xe6\xdb"
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend(),
)

key = base64.urlsafe_b64encode(kdf.derive(password))
print(key)


message = "jorson chuj"
encoded = message.encode()

f = Fernet(key)
encrypted = f.encrypt(encoded)

file = open("xd.txt", "wb")
file.write(encrypted)
file.close()

"""file = open("xd.txt", "rb")
enc = file.read()
file.close()
f2 = Fernet(key)
decrypted = f2.decrypt(enc)
org = decrypted.decode()
print(org)
"""
