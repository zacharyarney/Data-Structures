class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        new_node = BinarySearchTree(value)
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = new_node
        if value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = new_node
        # ITERATIVE
        # while self is not None:
        #     if value < self.value:
        #         if self.left is None:
        #             self.left = new_node
        #             return
        #         self = self.left
        #     if value > self.value:
        #         if self.right is None:
        #             self.right = new_node
        #             return
        #         self = self.right

    def contains(self, target):
        if target < self.value:
            if self.left:
                print(f'LEFT {self.left.value}')
                return self.left.contains(target)
            else:
                return False
        if target > self.value:
            if self.right:
                print(f'RIGHT {self.right.value}')
                return self.right.contains(target)
            else:
                return False
        if target == self.value:
            return True
        # ITERATIVE
        # while self is not None:
        #     if target < self.value:
        #         self = self.left
        #     if target > self.value:
        #         self = self.right
        #     if target == self.value:
        #         return True
        # return False

    def get_max(self):
        while self.right:
            self = self.right
        return self.value
