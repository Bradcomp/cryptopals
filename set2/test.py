import unittest
from hypothesis import given
from hypothesis.strategies import text, integers
from pks7padding import pks_7
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



if __name__ == '__main__':
    unittest.main()
