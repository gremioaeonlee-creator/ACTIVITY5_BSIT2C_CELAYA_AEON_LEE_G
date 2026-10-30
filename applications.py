from linked_stack import LinkedStack
from linked_queue import LinkedQueue


def is_balanced(text):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = LinkedStack()
    for char in text:
        if char in "([{":
            stack.push(char)
        elif char in pairs:
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    return stack.is_empty()


def simulate_print_queue(jobs):
    queue = LinkedQueue()
    for job_id, pages in jobs:
        queue.enqueue((job_id, pages))
        print("Enqueued job " + str(job_id) + " (" + str(pages) + " pages)")
    print()
    order = 1
    pages_before = 0
    while not queue.is_empty():
        job_id, pages = queue.dequeue()
        print(
            "Print order " + str(order) + ": job " + str(job_id)
            + " (" + str(pages) + " pages), waited behind "
            + str(pages_before) + " pages"
        )
        pages_before = pages_before + pages
        order = order + 1
    print("Total pages printed: " + str(pages_before))


def run_balanced_checker():
    print("\n--- Balanced Parentheses Checker ---")
    while True:
        text = input("Enter a string (blank to go back): ")
        if text == "":
            return
        if is_balanced(text):
            print("Balanced")
        else:
            print("Not balanced")


def run_print_queue():
    print("\n--- Print Queue Simulation ---")
    jobs = []
    while True:
        job_id = input("Enter job ID (blank to finish): ").strip()
        if job_id == "":
            break
        pages_text = input("Enter page count: ").strip()
        if not pages_text.isdigit() or int(pages_text) < 1:
            print("Page count must be a positive whole number")
            continue
        jobs.append((job_id, int(pages_text)))
    if not jobs:
        print("No jobs entered")
        return
    print()
    simulate_print_queue(jobs)
