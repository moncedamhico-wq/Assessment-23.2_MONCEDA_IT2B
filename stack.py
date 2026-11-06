def main():
    lastname = input("Enter your last name: ").strip().upper()

    if not lastname.isalpha():
        print("Please enter letters only.")
        return

    stack = []

    print("\n--- PUSH PHASE ---")

    for letter in lastname:
        stack.append(letter)

    print("All letters inserted successfully!")
    print("Stack:", stack)

    print("\n--- POP PHASE ---")

    while len(stack) > 0:
        input("Press ENTER to delete one letter: ")
        removed = stack.pop()
        print("Deleted:", removed)
        print("Current Stack:", stack)

    print("\nFinal Stack: []")
    print("Stack is Empty!")


if __name__ == "__main__":
    main()