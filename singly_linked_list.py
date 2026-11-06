class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def delete(self):
        if self.head is None:
            return None

        removed = self.head.data
        self.head = self.head.next
        return removed

    def display(self):
        current = self.head

        if current is None:
            print("NULL")
            return

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("NULL")


def main():
    linked_list = SinglyLinkedList()

    lastname = input("Enter your last name: ").strip().upper()

    if not lastname.isalpha():
        print("Please enter letters only.")
        return

    print("\n--- INSERTION PHASE ---")

    for letter in lastname:
        linked_list.append(letter)

    print("All letters inserted successfully!")
    linked_list.display()

    print("\n--- DELETION PHASE ---")

    while linked_list.head is not None:
        input("Press ENTER to delete one letter: ")
        removed = linked_list.delete()
        print("Deleted:", removed)
        print("Current List:")
        linked_list.display()

    print("\nFinal List: NULL")
    print("List is Empty!")


if __name__ == "__main__":
    main()