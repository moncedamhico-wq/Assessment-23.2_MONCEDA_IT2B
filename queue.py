from collections import deque


def main():
    lastname = input("Enter your last name: ").strip().upper()

    if not lastname.isalpha():
        print("Please enter letters only.")
        return

    queue = deque(lastname)

    print("\n--- ENQUEUE PHASE ---")
    print("All letters inserted successfully!")
    print("Queue:", list(queue))

    print("\n--- DEQUEUE PHASE ---")

    while len(queue) > 0:
        input("Press ENTER to delete one letter: ")
        removed = queue.popleft()
        print("Deleted:", removed)
        print("Current Queue:", list(queue))

    print("\nFinal Queue: []")
    print("Queue is Empty!")


if __name__ == "__main__":
    main()