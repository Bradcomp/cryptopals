from utils import compose
import array
def xor_arrays(a1, a2):
    return [a^b for (a, b) in zip(a1, a2)]

def to_bin(s):
    return ''.join(bin(x)[2:] for x in s)

def sum_bin_str(binstr):
    return reduce(lambda acc, x: acc + int(x), binstr, 0)

sum_xored_strings = compose(sum_bin_str, to_bin)

def hamming_distance(a1, a2):
        return sum_xored_strings(xor_arrays(a1, a2))

def test():
    assert hamming_distance(array.array('B', 'hello'), array.array('B', 'hello')) == 0
    assert hamming_distance(array.array('B', 'this is a test'), array.array('B', 'wokka wokka!!!')) == 37
