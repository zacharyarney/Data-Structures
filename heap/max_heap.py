class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        # deleted = self.get_max()
        store = self.storage
        store[0], store[len(store) - 1] = store[len(store) - 1], store[0]
        self._sift_down()
        store.pop()

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        store = self.storage
        parent = (index - 1) // 2
        if parent >= 0:
            if store[index] > store[parent]:
                store[index], store[parent] = store[parent], store[index]
                return self._bubble_up(parent)
            else:
                return

    def _sift_down(self, index):
        store = self.storage
        lc = (index * 2) + 1
        rc = (index * 2) + 2
        if lc < len(store):
            if rc < len(store):
                if store[rc] > store[lc]:
                    if store[rc] > store[index]:
                        store[index], store[rc] = store[rc], store[index]
                        return self._sift_down(rc)
                    else:
                        return
                if store[lc] > store[rc]:
                    if store[lc] > store[index]:
                        store[index], store[lc] = store[lc], store[index]
                        return self._sift_down(lc)
                    else:
                        return
