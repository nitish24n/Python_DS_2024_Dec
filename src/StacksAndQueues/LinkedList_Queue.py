class Node:
    """node class"""

    def __init__(self, elem):
        self.data = elem
        self.next = None


class Queue:
    def __init__(self, name):
        self.head = None
        self.name = name
        print(f"Initialised a new queue named {name}")

    def is_empty(self):
        return self.head == None

    def push(self, elem):
        node = Node(elem)
        if self.head is None:
            # For first element
            self.head = node
        else:
            # Add element at head
            node.next = self.head
            self.head = node
        print(f"pushed {node.data}")

    def pop(self):
        if self.is_empty():
            print("Can't pop on empty queue")
        elif self.head.next == None:
            t_head_data = self.head.data
            self.head = None
            return t_head_data
        else:
            t_head = self.head
            while t_head.next != None:
                t_head = t_head.next
            tail_data = t_head.data
            t_head = None
            print(f"popped {tail_data}")
            return tail_data

    def printElements(self):
        t_head = self.head
        if not self.is_empty():
            print("queue elements : ", end=" ")
            while t_head != None:
                print(t_head.data, end=" ")
                t_head = t_head.next
            print()
        else:
            print(f"Nothing to print in empty queue {self.name}")


if __name__ == "__main__":
    queue1 = Queue("Queue 1")
    queue1.push(3)
    queue1.push(5)
    queue1.pop()
    queue1.printElements()
    queue1.push(7)
    queue1.push(9)
    queue1.printElements()

    queue2 = Queue("Queue 2")
    queue2.printElements()
    queue2.push(23)
    queue2.pop()
    queue2.pop()
    queue2.printElements()
