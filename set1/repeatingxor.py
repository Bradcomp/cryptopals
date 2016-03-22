
def repeating_xor(pt, key):
    expanded_key = key * (len(pt) / len(key) + 1)
    return "".join([chr(ord(a) ^ ord(b)) for (a, b) in zip(pt, expanded_key)])
