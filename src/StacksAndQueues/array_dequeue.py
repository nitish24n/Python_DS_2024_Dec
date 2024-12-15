class dequeue:
    def __init__(self, arr=[]):
        self.length = len(arr)
        self.arr = arr

    def pushStart(self, elem):
        self.arr.append(elem)
        self.length += 1

    def pushEnd(self, elem):
        self.arr.insert(0, elem)
        self.length += 1

    def popStart(self):
        if self.length > 0:
            start_elem = self.arr[0]
            self.arr = self.arr[1:]
            print(f"popped {start_elem} from start")
            self.length -= 1
            return start_elem

    def popEnd(self):
        if self.length > 0:
            end_elem = self.arr[self.length - 1]
            self.arr = self.arr[:-1]
            print(f"popped {end_elem} from end")
            self.length -= 1
            return end_elem

    def print_elements(self):
        """prints queue elements"""
        print(f"Queue : {self.arr}")


# main method
if __name__ == "__main__":
    queue_length = input("Length of Queue : \n")

    queue_string_input = input(f"Enter {queue_length} elements separated by comma : \n")

    queue_elements = queue_string_input.split(",")
    queue = dequeue(queue_elements)

    queue.print_elements()
    queue.popStart()
    queue.print_elements()

    queue.popEnd()
    queue.print_elements()
