from Crypto.Cipher import AES
from array import array
from pks7padding import pks_7
from utils import xor_bytes, process_base64_file

def encrypt_block(block, key):
    cipher = AES.new(key, AES.MODE_ECB, '')
    return array('B', cipher.encrypt(block))

def decrypt_block(block, key):
    cipher = AES.new(key, AES.MODE_ECB, '')
    return array('B', cipher.decrypt(block))

#Once again, we assume everything is in byte arrays
def encrypt_aes_cbc(key, iv, bytes):
    if len(bytes) == 0:
        return array('B', [])
    block_size = len(iv)
    padded_bytes = pks_7(bytes, block_size)
    current = encrypt_block(xor_bytes(iv, padded_bytes[:block_size]), key)
    return current + encrypt_aes_cbc(key, current, padded_bytes[block_size:])

def decrypt_aes_cbc(key, iv, bytes):
    if len(bytes) == 0:
        return array('B', [])
    block_size = len(iv)
    current = xor_bytes(iv, decrypt_block(bytes[:block_size], key))
    return current + decrypt_aes_cbc(key, bytes[:block_size], bytes[block_size:])

def test():
    ct = process_base64_file('part10.txt')
    iv = array('B', [0] * 16)
    key = array('B', 'YELLOW SUBMARINE')
    pt = decrypt_aes_cbc(key, iv, ct)
    print pt.tostring()
    assert encrypt_aes_cbc(key, iv, pt) == ct
