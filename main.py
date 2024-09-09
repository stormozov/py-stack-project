class Stack:
    """Implements an efficient last-in first-out (LIFO) stack Abstract Data Type

    Supports the following operations:
    - isEmpty: Check if the stack is empty.
    - push: Add an item to the top of the stack.
    - pop: Remove and return the item at the top of the stack.
    - peek: Return the item at the top of the stack without removing it.
    - size: Return the number of items in the stack.
    """
    def __init__(self) -> None:
        """Initializes an empty stack.

        The stack is initially empty.
        """
        self.items = []

    def isEmpty(self) -> bool:
        """Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.items == []

    def push(self, item: object) -> None:
        """Add an item to the top of the stack.

        Args:
            item: The item to be added to the stack.
        """
        self.items.append(item)

    def pop(self) -> object:
        """Remove and return the item at the top of the stack.

        Returns:
            The item at the top of the stack.
        """
        return None if self.isEmpty() else self.items.pop()

    def peek(self) -> object:
        """Return the item at the top of the stack without removing it.

        Returns:
            The item at the top of the stack if the stack is not empty,
                None otherwise.
        """
        if not self.isEmpty():
            return self.items[self.size() - 1]

    def size(self) -> int:
        """Return the number of items in the stack.

        Returns:
            int: The number of items in the stack.
        """
        return len(self.items)


