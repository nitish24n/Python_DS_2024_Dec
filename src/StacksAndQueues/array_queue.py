from typing import List


class Queue:
    """Queue class"""

    def __init__(self):
        """initialise parameters"""
        self.queue = []

    def push(self, elem):
        """adds single element"""
        self.queue.append(elem)

    def push(self, elem: List):
        """appends list to queue"""
        self.queue.extend(elem)

    def pop(self):
        """pops element from queue & return its value"""
        if len(self.queue) > 0:
            pop_elem = self.queue[0]
            self.queue = self.queue[1:]
            return pop_elem

    def print_elements(self):
        """prints queue elements"""
        print(f"Queue : {self.queue}")


# main method
if __name__ == "__main__":
    queue_length = input("Length of Queue : \n")
    queue_string_input = input(f"Enter {queue_length} elements separated by comma : \n")

    queue_elements = queue_string_input.split(",")
    queue = Queue()
    queue.push(queue_elements)
    queue.print_elements()
    print(queue.pop())
    queue.print_elements()
