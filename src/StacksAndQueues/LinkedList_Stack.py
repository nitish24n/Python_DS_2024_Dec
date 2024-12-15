class Node:
    """node class"""

    def __init__(self, elem):
        self.data = elem
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, elem):
        node = Node(elem)
        # For first element
        if self.head is None:
            self.head = node
        else:
            # Add element at head
            node.next = self.head
            self.head = node

    def pop(self):
        current_data = self.head.data
        self.head = self.head.next
        return current_data

    def printElements(self):
        t_head = self.head
        if t_head == None:
            print("Empty Linked List")
        while t_head != None:
            print(t_head.data, end=" ")
            t_head = t_head.next
        print()


if __name__ == "__main__":
    stack = Stack()
    stack.push(3)
    stack.push(5)
    print(f"popped : {stack.pop()}")
    stack.push(7)
    stack.push(9)
    stack.printElements()
