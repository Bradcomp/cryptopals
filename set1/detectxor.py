from singlebytexor import likely_strings

def detect_xor(fname):
    final, best = None, 0
    for i, line in enumerate(file(fname, 'r')):
        result, score = likely_strings(line.strip())
        if score > best:
            final, best = result, score
    return final
