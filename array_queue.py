class ArrayQueue:
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity must be at least 1")
        self.data = [None] * capacity
        self.front = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == len(self.data)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue overflow: cannot enqueue into a full queue")
        rear = (self.front + self.size) % len(self.data)
        self.data[rear] = value
        self.size = self.size + 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue from an empty queue")
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size = self.size - 1
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty: nothing to peek at")
        return self.data[self.front]

    def state(self):
        items = []
        for offset in range(self.size):
            items.append(str(self.data[(self.front + offset) % len(self.data)]))
        shown = " | ".join(items) if items else "(empty)"
        return (
            "Queue (front to rear): " + shown + "\n"
            "Array: " + str(self.data)
            + "  front index = " + str(self.front)
            + "  size = " + str(self.size)
        )
