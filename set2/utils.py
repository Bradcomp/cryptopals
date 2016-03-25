from array import array

def process_base64_file(fname):
    return array('B', "".join(line for line in file(fname, 'r')).decode('base64'))

def xor_bytes(a1, a2):
    return array('B', [a^b for (a, b) in zip(a1, a2)])
