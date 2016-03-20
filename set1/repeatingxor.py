from fixedxor import fixed_xor

def repeating_xor(pt, key):
    hex_pt = pt.encode('hex')
    hex_key = key.encode('hex')
    return fixed_xor(hex_pt, hex_key * (len(hex_pt) / len(hex_key) + 1))
