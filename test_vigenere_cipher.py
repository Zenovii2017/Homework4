from vigenere_cipher import *
import unittest
from unittest import TestCase


class Test_vigenere_cipher(TestCase):
    def test_encode(self):
        """
        test encode function
        """
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("ENCODEDINPYTHON")
        self.assertEqual(encoded, "XECWQXUIVCRKHWA")

    def test_encode_character(self):
        """
        Test coding of two letters
        """
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("E")
        self.assertEqual(encoded, "X")

    def test_encode_spaces(self):
        """
        test encode text with free spaces
        """
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("ENCODED IN PYTHON")
        self.assertEqual(encoded, "XECWQXUIVCRKHWA")

    def test_encode_lowercase(self):
        """
        test encode test with small letters
        """
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("encoded in Python")
        self.assertEqual(encoded, "XECWQXUIVCRKHWA")

    def test_combine_character(self):
        """
        test combining two letters
        """
        encoded = VigenereCipher("").combine_character("E", "T")
        self.assertEqual(encoded, "X")
        encoded = VigenereCipher("").combine_character("N", "R")
        self.assertEqual(encoded, "E")

    def test_extend_keyword(self):
        """
        test extend bigger keyword
        """
        cipher = VigenereCipher("TRAIN")
        extended = cipher.extend_keyword(16)
        self.assertEqual(extended, "TRAINTRAINTRAINT")

    def test_separate_character(self):
        """
        test decode letter from two letters
        """
        encoded = VigenereCipher("").separate_character("X", "T")
        self.assertEqual(encoded, "E")
        encoded = VigenereCipher("").separate_character("E", "R")
        self.assertEqual(encoded, "N")

    def test_decode(self):
        """
        test decode function
        """
        cipher = VigenereCipher("TRAIN")
        decoded = cipher.decode("XECWQXUIVCRKHWA")
        self.assertEqual(decoded, "ENCODEDINPYTHON")

if __name__ == '__main__':
    unittest.main()
