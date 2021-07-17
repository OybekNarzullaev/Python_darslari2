from typing import Tuple
import os
import hashlib
import hmac

def hash_new_password(password: str) -> Tuple[bytes, bytes]:
    """
    Taqdim etilgan parolni tasodifiy ishlab chiqarilgan tuz bilan yuving va qaytaring
    ma'lumotlar bazasida saqlash uchun tuz va xash.
    """
    salt = os.urandom(16)
    pw_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt, pw_hash

def is_correct_password(salt: bytes, pw_hash: bytes, password: str) -> bool:
    """
    Oldindan saqlangan tuz va xash va foydalanuvchi tomonidan taqdim etilgan parol berilgan
    kirishga urinib ko'ring, parol to'g'ri yoki yo'qligini tekshiring.
    """
    return hmac.compare_digest(
        pw_hash,
        hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    )

# Example usage:
salt, pw_hash = hash_new_password('correct horse battery staple')
is_correct_password(salt, pw_hash, 'correct horse battery staple')
is_correct_password(salt, pw_hash, 'Tr0ub4dor&3')
is_correct_password(salt, pw_hash, 'rosebud')
print(pw_hash)
print(salt)
