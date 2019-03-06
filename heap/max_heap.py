class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        pass

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        store = self.storage
        parent = (index - 1) // 2
        if parent:
            if store[index] > store[parent]:
                store[index], store[parent] = store[parent], store[index]
                return _bubble_up(parent)
            if store[index] < store[parent]:
                return

    def _sift_down(self, index):
        store = self.storage
        lchild = (index * 2) + 1
        rchild = (index * 2) + 2
        if store[lchild] and store[rchild]:
            if store[rchild] > store[lchild]:
                if store[rchild] > store[index]:
                    store[index], store[rchild] = store[rchild], store[index]
                    return _sift_down(rchild)
                else:
                    return
            if store[lchild] > store[rchild]:
                if store[lchild] > store[index]:
                    store[index], store[lchild] = store[lchild], store[index]
                    return _sift_down(lchild)
                else:
                    return
