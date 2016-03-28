from array import array
#From here on out I deal with Byte arrays
def pks_7(bytes, block):
    if block == 0: return bytes
    padding_length = (block - len(bytes)) % block
    return bytes + array('B', [padding_length] * padding_length)
