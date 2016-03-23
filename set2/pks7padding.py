from array import array
#From here on out I deal with Byte arrays
def pks_7(bytes, block):
    padding_length = (block - len(bytes)) % block
    return bytes + array('B', [padding_length] * padding_length)

def test():
    bytes = array('B', 'YELLOW SUBMARINE')
    assert pks_7(bytes, 20).tostring() == 'YELLOW SUBMARINE\x04\x04\x04\x04'
    assert pks_7(bytes, 16).tostring() == 'YELLOW SUBMARINE'
    assert pks_7(bytes, 15).tostring() == 'YELLOW SUBMARINE\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e'
