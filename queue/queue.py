class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = LinkedList()

    def enqueue(self, item):
        self.storage.add_to_tail(item)
        self.size += 1

    def dequeue(self):
        if self.size:
            self.size -= 1
        return self.storage.remove_head()

    def len(self):
        return self.size


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        # make a new node with a value of value
        new_node = Node(value)
        # check to see if the linked list is empty
        # if so make head and tail equal to the new node
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # if head exists, make original head the self.next of new node
        else:
            new_node.next_node = self.head
            # set new node to head
            self.head = new_node

    def remove_head(self):
        # check to see if list is empty
        # if list is empty return None
        if not self.head and not self.tail:
            return None
        # if list has any items store a reference to the current head
        # if list is not empty check to see if list has only one item
        if self.head.get_next() is None:
            head = self.head
        # return current head value and set head and tail to none
            self.head = None
            self.tail = None
            return head
        # if list has more than one item
        else:
            head = self.head
        # return current head value
        # set self.head to current head's self.next
            self.head = self.head.get_next()
            return head

    def add_to_tail(self, value):
        # basically the same as add_to_head but backwards
        new_node = Node(value)
        if not self.tail and not self.head:
            self.tail = new_node
            self.head = new_node
        else:
            # we can use set next because we're inserting after the tail
            self.tail.set_next(new_node)
            self.tail = self.tail.get_next()

    def remove_tail(self):
        if not self.tail and not self.head:
            return None
        if self.tail == self.head:
            tail = self.tail
            self.tail = None
            self.head = None
            return tail
        else:
            tail = self.tail
