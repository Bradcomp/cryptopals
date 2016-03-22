from utils import process_base64_file
from Crypto.Cipher import AES

def decrypt_file(key, fname):
    cipher = AES.new(key, AES.MODE_ECB, '')
    ct = process_base64_file(fname)
    return cipher.decrypt(ct)

print decrypt_file(b'YELLOW SUBMARINE', 'part7.txt')
