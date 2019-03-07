"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_head(self, value):
        new_node = ListNode(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.insert_before(value)
            self.head = self.head.prev

    def remove_from_head(self):
        head = self.head.value
        if not self.head:
            return None
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev.delete()
        return head

    def add_to_tail(self, value):
        new_node = ListNode(value)
        if not self.tail and not self.head:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next

    def remove_from_tail(self):
        tail = self.tail.value
        if not self.tail:
            return None
        if self.tail == self.head:
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next.delete()
        return tail

    def move_to_front(self, node):
        val = node.value
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
        self.add_to_head(val)

    def move_to_end(self, node):
        val = node.value
        if node is self.head:
            self.remove_from_head()
        else:
            node.delete()
        self.add_to_tail(val)

    def delete(self, node):
        val = node.value
        if not self.head and not self.tail:
            return None
        if node is self.head:
            self.remove_from_head()
        if node is self.tail and self.tail != self.head:
            self.remove_from_tail()
        else:
            node.delete()
        return val

    def get_max(self):
        max = self.head
        current = self.head
        while current:
            if current.value > max.value:
                max = current
            current = current.next
        return max.value
