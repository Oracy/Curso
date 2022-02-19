import unittest

import test_examples.study.main as main

class TestMain(unittest.TestCase):
    def setUp(self):
        print('About to test a function')


    def test_do_stuff(self):
        '''Check if int + int is getting the right value'''
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)


    def test_do_stuff_2(self):
        test_param = 'a'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)


    def test_do_stuff_3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, "Please enter a number")
    

    def test_do_stuff_4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, "Please enter a number")


    def tearDown(self) -> None:
        print('Cleaning up')


if __name__ == '__main__':
    unittest.main()
