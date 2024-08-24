from pwdlib import PasswordHash

password_hash =  PasswordHash.recommended()

def get_password_hash(plain_password: str):
    return password_hash.hash(plain_password)

def get_password_verify(plain_password: str, hash_password: str):
    return password_hash.verify(plain_password, hash_password)