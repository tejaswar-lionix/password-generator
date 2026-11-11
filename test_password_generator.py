import string
import unittest

from password_generator import generate, strength


class PasswordTests(unittest.TestCase):
    def test_default_length(self):
        self.assertEqual(len(generate()), 16)

    def test_requested_length(self):
        self.assertEqual(len(generate(40)), 40)

    def test_uses_every_enabled_character_set(self):
        password = generate(64, upper=True, lower=True, digits=True, symbols=True)
        self.assertTrue(any(char in string.ascii_lowercase for char in password))
        self.assertTrue(any(char in string.ascii_uppercase for char in password))
        self.assertTrue(any(char in string.digits for char in password))
        self.assertTrue(
            any(char not in string.ascii_letters + string.digits for char in password)
        )

    def test_rejects_short_passwords(self):
        with self.assertRaises(ValueError):
            generate(3)

    def test_rejects_empty_character_sets(self):
        with self.assertRaises(ValueError):
            generate(8, upper=False, lower=False, digits=False, symbols=False)

    def test_strength_increases_with_variety(self):
        self.assertLess(strength("aaaaaaaa"), strength("aA1!aA1!"))


class PassphraseTests(unittest.TestCase):
    def test_passphrase_word_count(self):
        from password_generator import generate_passphrase

        passphrase = generate_passphrase(words=5, separator="-", capitalize=False)
        self.assertEqual(len(passphrase.split("-")), 5)

    def test_passphrase_requires_three_words(self):
        from password_generator import generate_passphrase

        with self.assertRaises(ValueError):
            generate_passphrase(words=2)

    def test_passphrase_capitalizes_words(self):
        from password_generator import generate_passphrase

        for word in generate_passphrase(words=4, capitalize=True).split("-"):
            self.assertEqual(word, word.capitalize())


if __name__ == "__main__":
    unittest.main()
