import unittest
from hypothesis import given
from hypothesis.strategies import text, integers
from pks7padding import pks_7
from cbcmode import encrypt_aes_cbc
from ecbcbcoracle import encrypt_aes_ecb, detector, make_black_box
from array import array

class PKS_7_Padding(unittest.TestCase):
    def test_basic_usage(self):
        bytes = array('B', 'YELLOW SUBMARINE')
        self.assertEqual(pks_7(bytes, 20).tostring(), 'YELLOW SUBMARINE\x04\x04\x04\x04')
        self.assertEqual(pks_7(bytes, 16).tostring(), 'YELLOW SUBMARINE')
        self.assertEqual(pks_7(bytes, 15).tostring(), 'YELLOW SUBMARINE\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e')

    @given(s=text(), padding=integers(min_value=1, max_value=255))
    def test_length_properties(self, s, padding):
        bytes = array('B', s.encode('ascii', 'replace'))
        padded_bytes = pks_7(bytes, padding)
        self.assertEqual(len(padded_bytes) % padding, 0)

class ECB_Detector(unittest.TestCase):
    def test_ecb_detection(self):
        always_ecb = make_black_box([encrypt_aes_ecb])
        always_cbc = make_black_box([encrypt_aes_cbc])
        for _ in range(100):
            self.assertEqual(detector(always_ecb), 'ECB')
        for _ in range(100):
            self.assertEqual(detector(always_cbc), 'NOT ECB')


if __name__ == '__main__':
    unittest.main()
