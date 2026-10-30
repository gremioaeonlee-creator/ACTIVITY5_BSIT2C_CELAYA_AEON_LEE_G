class ArrayStack:
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity must be at least 1")
        self.data = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.data) - 1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack overflow: cannot push onto a full stack")
        self.top = self.top + 1
        self.data[self.top] = value

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from an empty stack")
        value = self.data[self.top]
        self.data[self.top] = None
        self.top = self.top - 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: nothing to peek at")
        return self.data[self.top]

    def state(self):
        items = []
        index = self.top
        while index >= 0:
            items.append(str(self.data[index]))
            index = index - 1
        shown = " | ".join(items) if items else "(empty)"
        return (
            "Stack (top to bottom): " + shown + "\n"
            "Array: " + str(self.data) + "  top index = " + str(self.top)
        )
