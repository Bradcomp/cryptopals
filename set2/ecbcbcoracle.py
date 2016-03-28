from cbcmode import encrypt_aes_cbc, encrypt_block
from pks7padding import pks_7
from array import array
from random import randint
from utils import random_bytes

def encrypt_aes_ecb(key, bytes):
    padded_bytes = pks_7(array('B', bytes), 16)
    cipher = AES.new(key, AES.MODE_ECB, '')
    return array('B', cipher.encrypt(padded_bytes))

def encryption_oracle():
    prepad = random_bytes(randint(5, 10))
    postpad = random_bytes(randint(5, 10))
    key = random_bytes()
