from all_prefixes import *
import  unittest

class Test_prefixes(unittest.TestCase):
    def test_sentence(self):
        sentence = "lead"
        prefixes = all_prefixes(sentence)
        expected = set(['l', 'le', 'lea', 'lead'])
        self.assertEqual(prefixes, expected)
        sentence = "авангард"
        prefixes = all_prefixes(sentence)
        expected = set(['а', 'ав', 'ава', 'аван', 'аванг', 'аванга', 'авангар'\
                           , 'авангард', 'ан', 'анг', 'анга', 'ангар', 'ар',\
                        'ард', 'ангард'])
        self.assertEqual(prefixes, expected)

    def test_with_numbers(self):
        sentence = "lead1"
        prefixes = all_prefixes(sentence)
        expected = set(['l', 'le', 'lea', 'lead', 'lead1'])
        self.assertEqual(prefixes, expected)

    def test_with_upper_letters(self):
        sentence = 'Leadl'
        prefixes = all_prefixes(sentence)
        expected = set(['L', 'Le', 'Lea', 'Lead', 'Leadl'])
        self.assertEqual(prefixes, expected)

    def test_sentence_that_start_with_spaces(self):
        sentence = " lead"
        prefixes = all_prefixes(sentence)
        expected = set(['l', 'le', 'lea', 'lead'])
        self.assertEqual(prefixes, expected)

    def test_sentence_with_letters_from_different_languages(self):
        sentence = "andа"
        prefixes = all_prefixes(sentence)
        expected = set(['a', 'an', 'and', 'andа'])

if __name__ == '__main__':
    unittest.main()