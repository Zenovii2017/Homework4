class VigenereCipher:
    def __init__(self, keyword):
        """
        initialise class
        :param keyword: str
        """
        self.keyword = keyword

    def encode(self, plaintext):
        """
        encode text with Vignere method
        :param plaintext: str
        :return: str
        """
        plaintext = plaintext.replace(" ", "").upper()
        cipher = []
        keyword = self.extend_keyword(len(plaintext))
        for p, k in zip(plaintext, keyword):
            cipher.append(self.combine_character(p, k))
        return "".join(cipher)

    def extend_keyword(self, number):
        """
        make new plintext with lenght like text
        :param number: int
        :return: str
        """
        repeats = number // len(self.keyword) + 1
        return (self.keyword * repeats)[:number]

    @staticmethod
    def combine_character(plain, keyword):
        """
        make new letter with two comnined letters
        :param plain: str
        :param keyword: str
        :return: str
        """
        plain = plain.upper()
        keyword = keyword.upper()
        plain_num = ord(plain) - ord('A')
        keyword_num = ord(keyword) - ord('A')
        return chr(ord('A') + (plain_num + keyword_num) % 26)

    @staticmethod
    def separate_character(cypher, keyword):
        """
        decode one letter from recombined two another letters
        :param cypher: str
        :param keyword: str
        :return: str
        """
        cypher = cypher.upper()
        keyword = keyword.upper()
        cypher_num = ord(cypher) - ord('A')
        keyword_num = ord(keyword) - ord('A')
        return chr(ord('A') + (cypher_num - keyword_num) % 26)

    def decode(self, ciphertext):
        """
        decode encoded text with plaintext
        :param ciphertext: str
        :return: str
        """
        plain = []
        keyword = self.extend_keyword(len(ciphertext))
        for p, k in zip(ciphertext, keyword):
            plain.append(self.separate_character(p, k))
        return "".join(plain)
