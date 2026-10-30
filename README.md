# Stacks and Queues: Array vs. Linked List

**Name:** CELAYA, AEON LEE G.
**Section:** BSIT2C
**Activity:** Module 5 Laboratory Activity

## Description

This program implements two fundamental data structures in Python, each built twice: once on a fixed-size array and once on a singly linked list.

| Structure | Array version | Linked list version |
| --- | --- | --- |
| Stack (LIFO) | `ArrayStack` | `LinkedStack` |
| Queue (FIFO) | `ArrayQueue` (circular) | `LinkedQueue` |

It also includes a menu-driven program, a balanced parentheses checker that uses a stack, and a print queue simulation that uses a queue.

All structures are built from first principles. Python lists are only used as fixed-size storage for the array versions, never with `insert(0, x)` or `pop(0)`.

## Files

| File | Purpose |
| --- | --- |
| `node.py` | `Node` class shared by the linked stack and linked queue |
| `array_stack.py` | `ArrayStack` with `push`, `pop`, `peek`, `is_empty`, `is_full` |
| `linked_stack.py` | `LinkedStack` with the same operations and no fixed capacity |
| `array_queue.py` | Circular `ArrayQueue` with `enqueue`, `dequeue`, `peek_front`, `is_empty`, `is_full` |
| `linked_queue.py` | `LinkedQueue` with head and tail references |
| `applications.py` | Balanced parentheses checker and print queue simulation |
| `main.py` | Menu-driven program |
| `test_driver.py` | Automatic test driver that demonstrates every operation and error |
| `sample_runs.txt` | Output of `test_driver.py` showing underflow, overflow, and wrap-around |
| `analysis.md` | Written answer to the analysis question |

## Requirements

Python 3.8 or newer. No external libraries are needed.

## How to Run

Put all files in the same folder, open a terminal in that folder, and run the commands below.

### Menu-driven program

```
python main.py
```

1. Choose an implementation from the main menu:
   - `1` ArrayStack
   - `2` LinkedStack
   - `3` ArrayQueue
   - `4` LinkedQueue
   - `5` Balanced parentheses checker
   - `6` Print queue simulation
   - `0` Exit
2. For the array versions, enter a capacity when asked.
3. Choose an operation. The state of the structure is printed after each operation.
4. Enter `0` to return to the main menu.

### ArrayStack and LinkedStack

Operations: `push`, `pop`, `peek`, `is_empty`, `is_full`.
The stack is shown from top to bottom. Popping an empty stack reports a stack underflow, and pushing onto a full `ArrayStack` reports a stack overflow.

### ArrayQueue and LinkedQueue

Operations: `enqueue`, `dequeue`, `peek_front`, `is_empty`, `is_full`.
The queue is shown from front to rear. `ArrayQueue` also shows the raw array, the front index, and the size, so wrap-around is visible once items are enqueued past the end of the array. Dequeuing from an empty queue reports a queue underflow, and enqueuing into a full `ArrayQueue` reports a queue overflow.

### Balanced parentheses checker

Choose `5` in the main menu and type any string containing `()`, `[]`, and `{}`. The program reports whether the brackets are balanced. Press Enter on a blank line to go back.

### Print queue simulation

Choose `6` in the main menu. Enter a job ID and page count for each job, and press Enter on a blank job ID to finish. The jobs are printed in the order they were submitted, and the program reports each job's print order and how many pages it waited behind.

### Test driver

```
python test_driver.py
```

This runs every operation on all four structures without any input, including underflow, overflow, and circular wrap-around. The output is saved in `sample_runs.txt`.

## Error Handling

| Condition | Exception raised | Message |
| --- | --- | --- |
| Pop on an empty stack | `IndexError` | Stack underflow |
| Peek on an empty stack | `IndexError` | Stack is empty |
| Push onto a full `ArrayStack` | `OverflowError` | Stack overflow |
| Dequeue on an empty queue | `IndexError` | Queue underflow |
| Peek on an empty queue | `IndexError` | Queue is empty |
| Enqueue into a full `ArrayQueue` | `OverflowError` | Queue overflow |

## Sample Run

Excerpt from `sample_runs.txt` showing circular wrap-around in `ArrayQueue` with capacity 4:

```
enqueue(E)
Queue (front to rear): C | D | E
Array: ['E', None, 'C', 'D']  front index = 2  size = 3
enqueue(F)
Queue (front to rear): C | D | E | F
Array: ['E', 'F', 'C', 'D']  front index = 2  size = 4
```

See `sample_runs.txt` for the full output.
