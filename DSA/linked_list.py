# Linked List Implementation in Python
# Beginner-friendly with clear explanations

# Node class represents each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data      # Stores the value
        self.next = None      # Points to the next node (default: None)

# LinkedList class manages the nodes
class LinkedList:
    def __init__(self):
        self.head = None      # Start of the list (initially empty)

    # Insert a new node at the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:         # If list is empty
            self.head = new_node
            return
        last = self.head
        while last.next:              # Traverse till the last node
            last = last.next
        last.next = new_node

    # Insert a new node at the beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head     # New node points to old head
        self.head = new_node          # Head updated to new node

    # Delete a node by value
    def delete(self, key):
        temp = self.head

        # If head node itself holds the key
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        # Search for the key
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:   # Key not found
            return

        prev.next = temp.next
        temp = None

    # Print the linked list
    def display(self):
        nodes = []
        temp = self.head
        while temp:
            nodes.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(nodes))

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.prepend(5)
    ll.display()          # Output: 5 -> 10 -> 20 -> 30
    ll.delete(20)
    ll.display()          # Output: 5 -> 10 -> 30
