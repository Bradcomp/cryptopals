import array
from hammingdistance import hamming_distance
from utils import compose, letter_count, process_base64_file

def xor_bytes(a1, a2):
    return array.array('B', [a^b for (a, b) in zip(a1, a2)])

def decrypt_with_byte(b, s):
    return xor_bytes(s, [b] * (len(s)))

def good_letter(c):
    most_likely = list('etaoin shrd')
    if c in most_likely:
        return 1
    if ord(c) < 48 or ord(c) > 122:
        return -1
    return 0

def likely_score(s):
    counts = letter_count(s)
    return reduce(lambda acc, item: acc + (item[1] * good_letter(item[0])), counts, 0)

def likely_strings(ct):
    results = map(compose(lambda x: (x, likely_score(x)), lambda x: x.tostring()), [decrypt_with_byte(b, ct) for b in range(256)])
    return reduce(lambda acc, x: acc if acc[1] > x[1] else x, results)[0]

def calc_hamming_distance(key_size, ciphertext):
    ham1 = hamming_distance(ciphertext[:key_size], ciphertext[key_size:key_size * 2])
    ham2 = hamming_distance(ciphertext[key_size:key_size * 2], ciphertext[key_size * 2:key_size * 3])
    ham3 = hamming_distance(ciphertext[:key_size], ciphertext[key_size * 2:key_size * 3])
    return (ham1 + ham2 + ham3) / (3.0 * key_size)

def find_key_size(ciphertext):
    return filter(
        lambda x: x[1] < 3,
        [(size, calc_hamming_distance(size, ciphertext)) for size in range(2, 41) if size < len(ciphertext) / 3]
    )

def decrypt_with_keysize(key_size, ciphertext):
    transposed = [ciphertext[n::key_size] for n in range(key_size)]
    transposed_plaintext = map(likely_strings, transposed)
    plaintext = "";
    for i in range(len(transposed_plaintext[0])):
        for j in range(len(transposed_plaintext)):
            try:
                plaintext += transposed_plaintext[j][i]
            except:
                continue
    return plaintext

def decrypt_file(fname):
    ciphertext = array.array('B', process_base64_file(fname))
    potentials = [decrypt_with_keysize(key_size[0], ciphertext) for key_size in find_key_size(ciphertext)]
    return reduce(lambda x, y: x if likely_score(x) > likely_score(y) else y, potentials)

print decrypt_file('part6.txt')
