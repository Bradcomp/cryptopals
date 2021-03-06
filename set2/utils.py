from array import array
from Crypto.Random import _UserFriendlyRNG as rng

def chunk(size, s):
    return (s[n * size:(n + 1) * size] for n in range(len(s) / size + 1))

def process_base64_file(fname):
    return array('B', "".join(line for line in file(fname, 'r')).decode('base64'))

def xor_bytes(a1, a2):
    return array('B', [a^b for (a, b) in zip(a1, a2)])

def random_bytes(block = 16):
    return array('B', rng.get_random_bytes(block))
