from node import Node


class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def is_full(self):
        return False

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from an empty stack")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: nothing to peek at")
        return self.top.value

    def state(self):
        items = []
        current = self.top
        while current is not None:
            items.append(str(current.value))
            current = current.next
        shown = " | ".join(items) if items else "(empty)"
        return "Stack (top to bottom): " + shown
