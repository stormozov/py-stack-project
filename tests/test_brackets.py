import unittest

from main import Stack


class TestBrackets(unittest.TestCase):
    def setUp(self):
        """Sets up a new instance of Stack before each test method is run.

        This ensures that each test method starts with a clean slate.
        """
        self.stack = Stack()

    @classmethod
    def tearDown(cls):
        """Reset the stack after all test methods have been run.

        This ensures that the stack does not retain any state between test runs.
        """
        Stack().items.clear()

    def test_is_balanced_brackets(self):
        """Tests that the stack is correctly identified as balanced or not.

        This test case ensures that the is_balanced_brackets method correctly
        identifies whether the stack is balanced or not.
        """
        test_cases = [
            ('(((([{}]))))', 'Сбалансированно'),
            ('[([])((([[[]]])))]{()}', 'Сбалансированно'),
            ('{{[()]}}', 'Сбалансированно'),
            ('}{}', 'Несбалансированно'),
            ('{{[(])]}}', 'Несбалансированно'),
            ('[[{())}]', 'Несбалансированно'),
        ]

        for input_str, expected_result in test_cases:
            self.assertEqual(
                self.stack.is_balanced_brackets(input_str),
                expected_result
            )
            print()
            print(f'Input: {input_str},\nExpected result: {expected_result}')


if __name__ == '__main__':
    unittest.main()
