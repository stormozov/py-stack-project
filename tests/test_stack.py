import unittest

from main import Stack


class TestStack(unittest.TestCase):
    """Test case class for testing the Stack class methods.

    Includes test methods for isEmpty, push, pop, peek, and size operations.
    """
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
        Stack().items = []

    def test_is_empty(self):
        """Tests that the stack is initially empty.

        This test case ensures that the isEmpty method correctly indicates
            whether the stack is empty or not.
        """
        self.assertTrue(self.stack.isEmpty())
        self.stack.push(1)
        self.assertFalse(self.stack.isEmpty())

    def test_push(self):
        """Tests that the stack contains one item after pushing an item.

        This test case ensures that the push method correctly adds an item to
            the stack and that the subsequent calls to size and peek methods
            return the expected results.
        """
        self.stack.push(1)
        self.assertEqual(self.stack.size(), 1)
        self.assertEqual(self.stack.peek(), 1)

    def test_pop(self):
        """Tests that the stack is empty after popping an item.

        This test case ensures that the pop method removes the top item from the
            stack and returns the correct value, and that the subsequent call to
            the size method returns the expected result.
        """
        self.stack.push(1)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.size(), 0)

    def test_peek(self):
        """Tests that the top item in the stack is returned correctly.

        This test case ensures that the peek method returns the correct
        value, and that the stack is not modified in the process.
        """
        self.stack.push(1)
        self.stack.push(2)
        print(f' Top item: {self.stack.peek()}')
        self.assertEqual(self.stack.peek(), 2)

    def test_size(self):
        """Tests that the size of the stack is correctly reported.

        This test case ensures that the size method returns the correct
        number of items in the stack.
        """
        self.stack.push(1)
        print(f' Stack size: {self.stack.size()}')
        self.assertEqual(self.stack.size(), 1)


if __name__ == '__main__':
    unittest.main()
