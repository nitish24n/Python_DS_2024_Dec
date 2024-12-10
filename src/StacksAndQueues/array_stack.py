from typing import List


class Stack:
    """stack class"""

    def __init__(self):
        """initialise parameters"""
        self.length = 0
        self.stack = []

    def push(self, elem):
        """adds single element"""
        self.stack.append(elem)
        self.length += 1

    def push(self, elem: List):
        """appends list to stack"""
        for i in elem:
            self.stack.append(i)
        self.length += len(elem)

    def pop(self):
        """pops element from stack & return its value"""
        if self.length > 0:
            self.length -= 1
            pop_elem = self.stack[self.length - 1]
            self.stack = self.stack[:-1]
            return pop_elem

    def print_elements(self):
        """prints stack elements"""
        print(f"Stack : {self.stack}")


# main method
if __name__ == "__main__":
    stack_length = input("Length of Stack : \n")
    stack_string_input = input(f"Enter {stack_length} elements separated by comma : \n")

    stack_elements = stack_string_input.split(",")
    stack = Stack()
    stack.push(stack_elements)
    stack.print_elements()
    stack.pop()
    stack.print_elements()
