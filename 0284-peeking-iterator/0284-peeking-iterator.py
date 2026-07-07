class PeekingIterator:
    def __init__(self, iterator):
        self.it = iterator
        self._next = self.it.next() if self.it.hasNext() else None

    def peek(self):
        return self._next

    def next(self):
        val = self._next
        self._next = self.it.next() if self.it.hasNext() else None
        return val

    def hasNext(self):
        return self._next is not None