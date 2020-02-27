from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.left.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        # make a queue
        queue = Queue()
        # save root to temp variable
        temp = node
        queue.enqueue(temp)

        # while something in queue
        while queue.size > 0:
            # pop off first item
            temp = queue.dequeue()
            # print item
            print(temp.value)

            # if temp.left
            if temp.left:
                # add temp left to queue
                queue.enqueue(temp.left)
            # if temp.right
            if temp.right:
                # add temp right to queue
                queue.enqueue(temp.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        # make a stack
        stack = Stack()
        temp = node
        # add root to stack
        stack.push(temp)
        # while something in stack
        while stack.size > 0:
            # pop off root and save in variable
            temp = stack.pop()
        # print value
            print(temp.value)
        # if temp left
            if temp.left:
                # push temp left ot stack
                stack.push(temp.left)
        # if temp right
            if temp.right:
                # push temp right to stack
                stack.push(temp.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            node.pre_order_dft(node.left)
        if node.right:
            node.pre_order_dft(node.right)
        # Print Post-order recursive DFT

    def post_order_dft(self, node):
        pass
