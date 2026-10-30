from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue
from applications import is_balanced, simulate_print_queue


def attempt(label, action):
    try:
        result = action()
        print(label + " -> " + str(result))
    except (IndexError, OverflowError) as error:
        print(label + " -> Error: " + str(error))


def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def test_array_stack():
    section("ArrayStack (capacity 3)")
    stack = ArrayStack(3)
    attempt("pop on empty", stack.pop)
    attempt("peek on empty", stack.peek)
    for value in ["A", "B", "C"]:
        stack.push(value)
        print("push(" + value + ")")
        print(stack.state())
    attempt("push(D) on full", lambda: stack.push("D"))
    attempt("peek", stack.peek)
    attempt("pop", stack.pop)
    print(stack.state())
    attempt("is_full", stack.is_full)
    attempt("is_empty", stack.is_empty)


def test_linked_stack():
    section("LinkedStack")
    stack = LinkedStack()
    attempt("pop on empty", stack.pop)
    attempt("peek on empty", stack.peek)
    for value in ["A", "B", "C"]:
        stack.push(value)
        print("push(" + value + ")")
        print(stack.state())
    attempt("peek", stack.peek)
    attempt("pop", stack.pop)
    attempt("pop", stack.pop)
    attempt("pop", stack.pop)
    print(stack.state())
    attempt("pop on empty", stack.pop)


def test_array_queue():
    section("ArrayQueue (capacity 4), circular wrap-around")
    queue = ArrayQueue(4)
    attempt("dequeue on empty", queue.dequeue)
    attempt("peek_front on empty", queue.peek_front)
    for value in ["A", "B", "C", "D"]:
        queue.enqueue(value)
        print("enqueue(" + value + ")")
        print(queue.state())
    attempt("enqueue(E) on full", lambda: queue.enqueue("E"))
    attempt("dequeue", queue.dequeue)
    attempt("dequeue", queue.dequeue)
    print(queue.state())
    print("Enqueuing past the physical end of the array:")
    queue.enqueue("E")
    print("enqueue(E)")
    print(queue.state())
    queue.enqueue("F")
    print("enqueue(F)")
    print(queue.state())
    attempt("peek_front", queue.peek_front)
    while not queue.is_empty():
        attempt("dequeue", queue.dequeue)
    print(queue.state())


def test_linked_queue():
    section("LinkedQueue")
    queue = LinkedQueue()
    attempt("dequeue on empty", queue.dequeue)
    attempt("peek_front on empty", queue.peek_front)
    for value in ["A", "B", "C"]:
        queue.enqueue(value)
        print("enqueue(" + value + ")")
        print(queue.state())
    attempt("peek_front", queue.peek_front)
    attempt("dequeue", queue.dequeue)
    attempt("dequeue", queue.dequeue)
    attempt("dequeue", queue.dequeue)
    print(queue.state())
    queue.enqueue("X")
    print("enqueue(X) after becoming empty")
    print(queue.state())
    attempt("dequeue", queue.dequeue)
    attempt("dequeue on empty", queue.dequeue)


def test_balanced():
    section("Application: balanced parentheses")
    samples = ["()", "([]{})", "(]", "((())", "{[()]}", ")(", "", "a(b)c[d]"]
    for text in samples:
        print(repr(text) + " -> " + ("Balanced" if is_balanced(text) else "Not balanced"))


def test_print_queue():
    section("Application: print queue simulation")
    simulate_print_queue([("J101", 5), ("J102", 12), ("J103", 3), ("J104", 8)])


if __name__ == "__main__":
    test_array_stack()
    test_linked_stack()
    test_array_queue()
    test_linked_queue()
    test_balanced()
    test_print_queue()
