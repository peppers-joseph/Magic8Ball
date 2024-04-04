import io
import unittest
from main import Magic8Ball as meb
import sys

class Magic8Test(unittest.TestCase):
    def setUp(self):
        self.m8 = meb.Magic8Ball()

    def test_get_random_number(self):
        for num in range(1000):
            rand_num = self.m8.get_random_number()
            #print(f"Random Number is: {rand_num}")
            self.assertTrue(rand_num in range(0,20))

    def test_get_response_valid_2(self):
        actual = self.m8.get_response(2)
        expected = "Without a doubt"
        self.assertEqual(actual, expected)

    def test_get_response_valid_3(self):
        actual = self.m8.get_response(3)
        expected = "Yes definitely"
        self.assertEqual(actual, expected)

    def test_get_response_invalid(self):
        with self.assertRaises(IndexError):
            actual = self.m8.get_response(22)

    def test_question_ends_with_mark(self):
        with self.assertRaises(ValueError):
            sim_stdin = sys.stdin
            sys.stdin = io.StringIO("This is not a question.")
            resp = self.m8.ask_a_question()
            sys.stdin = sim_stdin

    def test_question_ends_with_mark(self):
        sim_stdin = sys.stdin
        sys.stdin = io.StringIO("Will I pass this class?")
        resp = self.m8.ask_a_question()
        sys.stdin = sim_stdin
        self.assertIsNotNone(resp)
        #print(resp)

if __name__ == "__main__":
    unittest.main()
