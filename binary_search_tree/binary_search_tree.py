class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        pass

    def contains(self, target):
        while self is not None:
            if target < self.value:
                self = self.left
            if target > self.value:
                self = self.right
            if target == self.value:
                return True
        return False

    def get_max(self):
        pass
