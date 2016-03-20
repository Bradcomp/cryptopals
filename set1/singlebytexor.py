from fixedxor import fixed_xor
from utils import letter_count

ciphertext = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
most_likely = list('ETAOIN SHRD');

def decrypt_with_byte(s, b):
    return fixed_xor(s, b * (len(s) / len(b)))

def likely_strings(ct):
    for b in range(256):
        result = decrypt_with_byte(ct, hex(b)[2:])
        if letter_count(result)[0][0] in most_likely:
            return result
