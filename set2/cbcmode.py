from Crypto.Cipher import AES
from Crypto.Random import _UserFriendlyRNG as uf

def decrypt_file(key, fname):
    cipher = AES.new(key, AES.MODE_ECB, '')
    ct = process_base64_file(fname)
    return cipher.decrypt(ct)
