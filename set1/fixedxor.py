from binascii import b2a_hex

def fixed_xor(s1, s2):
    b1 = s1.decode('hex')
    b2 = s2.decode('hex')
    return "".join([chr(ord(a) ^ ord(b)) for (a, b) in zip(b1, b2)])
