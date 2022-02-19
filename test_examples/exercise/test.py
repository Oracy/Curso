import unittest
import main


class TestGame(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        res = main.run_guess(guess, answer)
        self.assertTrue(res)


    def test_input_wrong_guess(self):
        res = main.run_guess(5, 0)
        self.assertFalse(res)

    
    def test_input_wrong_number(self):
        res = main.run_guess(5, 11)
        self.assertFalse(res)


    def test_input_wrong_type(self):
        res = main.run_guess(5, 'z')
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()