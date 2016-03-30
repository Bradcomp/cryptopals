from array import array
from utils import random_bytes
from ecbcbcoracle import encrypt_aes_ecb, detector

secret_text = array('B', 'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK'.decode('base64'))

def make_ecb_black_box():
    key = random_bytes()
    def black_box(pt):
        pt = array('B', pt) + secret_text
        return encrypt_aes_ecb(key, '', pt)
    return black_box


def detect_block_size(cipher):
    pt = 'a'
    prev_block_size = current_block_size = len(cipher(pt))
    while prev_block_size == current_block_size:
        pt += 'a'
        prev_block_size, current_block_size = current_block_size, len(cipher(pt))
    prev_block_size = current_block_size
    start = len(pt)
    while prev_block_size == current_block_size:
        pt += 'a'
        prev_block_size, current_block_size = current_block_size, len(cipher(pt))
    return len(pt) - start

def decrypt_secret(cipher):
    block_size = detect_block_size(cipher)
    ct_length = len(cipher(array('B', [0] * block_size)))
    if detector(cipher, block_size) != 'ECB':
        raise ValueError('Tried to decrypt non-ECB cipher')
    current_byte = 1
    current_block = 0
    last_block = [0] * 16
    pt = []
    while current_block < ct_length / block_size:
        pt_block = []
        while current_byte <= block_size:
            lead = last_block[current_byte:block_size]
            first = cipher(array('B', lead))[block_size * current_block:block_size * (current_block + 1)]
            for b in range(256):
                test = cipher(array('B', lead + pt_block + [b]))[:block_size]
                if test == first:
                    pt_block += [b]
                    break
            current_byte += 1
        pt += pt_block
        last_block = pt_block[:]
        current_byte = 1
        current_block += 1
    print "".join(map(chr, pt))

if __name__ == '__main__':
    decrypt_secret(make_ecb_black_box())
