from cbcmode import encrypt_aes_cbc, encrypt_block
from Crypto.Cipher import AES
from pks7padding import pks_7
from array import array
from random import randint, choice
from utils import random_bytes, chunk

def encrypt_aes_ecb(key, iv, bytes):
    padded_bytes = pks_7(array('B', bytes), 16)
    cipher = AES.new(key, AES.MODE_ECB, '')
    return array('B', cipher.encrypt(padded_bytes))

def make_black_box(ciphers):
    def black_box(plaintext):
        prepad = random_bytes(randint(5, 10))
        postpad = random_bytes(randint(5, 10))
        key = random_bytes()
        iv = random_bytes()
        return choice(ciphers)(key, iv, prepad + plaintext + postpad)
    return black_box

encryption_oracle = make_black_box([encrypt_aes_ecb, encrypt_aes_cbc])

def detector(black_box, block_size=16):
    pt = array('B', 'A' * (block_size * 3))
    ct = black_box(pt)
    chunks = chunk(block_size, ct)
    nxt = chunks.next()
    for block in chunks:
        if len(block) and block == nxt:
            return 'ECB'
        nxt = block
    return 'NOT ECB'
