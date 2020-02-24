from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if not self.storage:
            return
        stack_item = self.storage.remove_from_tail()
        self.size -= 1
        return stack_item

    def len(self):
        return self.size
