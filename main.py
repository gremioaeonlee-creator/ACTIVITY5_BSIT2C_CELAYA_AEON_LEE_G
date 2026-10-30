from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue
from applications import run_balanced_checker, run_print_queue


def read_capacity():
    while True:
        text = input("Enter capacity: ").strip()
        if text.isdigit() and int(text) >= 1:
            return int(text)
        print("Capacity must be a positive whole number")


def run_structure(structure, title, add_name, remove_name, look_name):
    adder = getattr(structure, add_name)
    remover = getattr(structure, remove_name)
    looker = getattr(structure, look_name)
    while True:
        print("\n--- " + title + " ---")
        print("1. " + add_name)
        print("2. " + remove_name)
        print("3. " + look_name)
        print("4. is_empty")
        print("5. is_full")
        print("0. Back to main menu")
        choice = input("Choose an operation: ").strip()
        try:
            if choice == "1":
                value = input("Enter value: ")
                adder(value)
                print(add_name + "(" + value + ") done")
            elif choice == "2":
                print("Returned: " + str(remover()))
            elif choice == "3":
                print("Returned: " + str(looker()))
            elif choice == "4":
                print(str(structure.is_empty()))
            elif choice == "5":
                print(str(structure.is_full()))
            elif choice == "0":
                return
            else:
                print("Invalid choice")
                continue
        except (IndexError, OverflowError) as error:
            print("Error: " + str(error))
        print(structure.state())


def main():
    while True:
        print("\n===== Stacks and Queues =====")
        print("1. ArrayStack")
        print("2. LinkedStack")
        print("3. ArrayQueue (circular)")
        print("4. LinkedQueue")
        print("5. Balanced parentheses checker")
        print("6. Print queue simulation")
        print("0. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            run_structure(ArrayStack(read_capacity()), "ArrayStack", "push", "pop", "peek")
        elif choice == "2":
            run_structure(LinkedStack(), "LinkedStack", "push", "pop", "peek")
        elif choice == "3":
            run_structure(ArrayQueue(read_capacity()), "ArrayQueue", "enqueue", "dequeue", "peek_front")
        elif choice == "4":
            run_structure(LinkedQueue(), "LinkedQueue", "enqueue", "dequeue", "peek_front")
        elif choice == "5":
            run_balanced_checker()
        elif choice == "6":
            run_print_queue()
        elif choice == "0":
            print("Goodbye")
            return
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
