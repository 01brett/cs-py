class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        size = len(self.storage)
        if size == 0:
            self.storage.append(value)
            return
        root = self.storage[0]
        if value > root:
            self.storage

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        pass

    def _sift_down(self, index):
        pass
