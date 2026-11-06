def main():
    lastname = input("Enter your last name: ").strip().upper()

    if not lastname.isalpha() or len(lastname) > 8:
        print("Please enter a valid last name (maximum 8 letters).")
        return

    arr = list(lastname)

    print("\n--- INSERTION PHASE ---")
    print("All letters inserted successfully!")
    print("Array:", arr)

    print("\n--- DELETION PHASE ---")

    while len(arr) > 0:
        input("Press ENTER to delete one letter: ")
        removed = arr.pop(0)
        print("Deleted:", removed)
        print("Current Array:", arr)

    print("\nFinal Array: []")
    print("Array is Empty!")


if __name__ == "__main__":
    main()