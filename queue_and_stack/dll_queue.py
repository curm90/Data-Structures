from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def dequeue(self):
        if not self.size:
            return

        queue_item = self.storage.remove_from_tail()
        self.size -= 1
        return queue_item

    def len(self):
        return self.size
