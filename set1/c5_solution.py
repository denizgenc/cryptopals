from c5_repeating_key import repeating_key
import unittest

string_1 = "Burning 'em, if you ain't quick and nimble"
string_2 = "I go crazy when I hear a cymbal"

# It turns out that the problem expected the string to have both lines
string_combined = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""

key = "ICE"
encrypted_1 = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272"
encrypted_2 = "a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

class TestXorEncoding(unittest.TestCase):
#    def test1(self):
#        self.assertEqual(encrypted_1, repeating_key(string_1, key))
#
#    def test2(self):
#        self.assertEqual(encrypted_2, repeating_key(string_2, key))

    def test_combined(self):
        self.assertEqual(encrypted_1 + encrypted_2,
                         repeating_key(string_combined, key))

if __name__ == '__main__':
    unittest.main()
