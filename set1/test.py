from fixedxor import fixed_xor
import singlebytexor as sb

def part2():
    result = fixed_xor('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965')
    assert result.encode('hex') == '746865206b696420646f6e277420706c6179'

def part3():
    plaintext, _ = sb.likely_strings(sb.ciphertext)
    assert plaintext == "Cooking MC's like a pound of bacon"

def test():
    part2()
    part3()

test()
