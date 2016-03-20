from binascii import b2a_hex

def fixed_xor(s1, s2):
    b1 = s1.decode('hex')
    b2 = s2.decode('hex')
    return "".join([chr(ord(a) ^ ord(b)) for (a, b) in zip(b1, b2)])

def test():
    result = fixed_xor('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965')
    print result
    assert result.encode('hex') == '746865206b696420646f6e277420706c6179'
