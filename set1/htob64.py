from binascii import a2b_hex, b2a_base64
from utils import compose

hex_to_base64 = compose(b2a_base64, a2b_hex)
