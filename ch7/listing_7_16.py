"""
Хеширование паролей с помощью алгоритма `scrypt`

Sample output:
Total time: 36.6953
"""
import hashlib
import os
import random
import string
import time


def random_password(length: int) -> str:
    ascii_lowercase = string.ascii_lowercase
    return "".join(random.choice(ascii_lowercase) for _ in range(length))


passwords = [random_password(10) for _ in range(10000)]


def hash(password: bytes) -> str:
    salt = os.urandom(16)
    return str(hashlib.scrypt(password, salt=salt, n=2048, p=1, r=8))


start = time.time()

[hash(bytes(password, encoding="utf-8")) for password in passwords]

end = time.time()
print(f"Total time: {end-start:.4f}")
