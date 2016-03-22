def chunk(size, s):
    return filter(len, [s[n * size:(n + 1) * size] for n in range(len(s) / size + 1)])

def detect_ecb(fname):
    for i, line in enumerate(open(fname, 'r')):
        ct_chunks = chunk(16, line.strip().decode('hex'))
        if len(set(ct_chunks)) < len(ct_chunks):
            print i + 1, "".join(ct_chunks)

detect_ecb('part8.txt')
