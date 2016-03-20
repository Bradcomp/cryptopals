from fixedxor import fixed_xor
from utils import letter_count

ciphertext = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
most_likely = list('ETAOIN SHRD'.lower());

def decrypt_with_byte(s, b):
    return fixed_xor(s, b * (len(s) / len(b)))

def likely_score(s):
    counts = letter_count(s)
    return reduce(lambda acc, item: acc + item[1] if item[0] in most_likely else acc, counts, 0)

def likely_strings(ct):
    final, best = None, 0

    for b in range(256):
        result = decrypt_with_byte(ct, hex(b)[2:])
        score = likely_score(result)
        if score > best:
            final, best = result, score
    return final, best
