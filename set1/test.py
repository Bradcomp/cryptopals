from fixedxor import fixed_xor
from repeatingxor import repeating_xor
import singlebytexor as sb

def part2():
    result = fixed_xor('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965')
    assert result.encode('hex') == '746865206b696420646f6e277420706c6179'

def part3():
    plaintext, _ = sb.likely_strings(sb.ciphertext)
    assert plaintext == "Cooking MC's like a pound of bacon"

def part5():
    pt1 = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"
    print repeating_xor(pt1, key).encode('hex')
    assert repeating_xor(pt1, key).encode('hex') == "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

def test():
    part2()
    part3()
    part5()

test()
