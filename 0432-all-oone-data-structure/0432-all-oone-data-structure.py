class Node:
    def __init__(self, cnt):
        self.cnt = cnt
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_count = {}
        self.count_node = {}

    def _add_after(self, node, new_node):
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key not in self.key_count:
            self.key_count[key] = 1

            if 1 not in self.count_node:
                node = Node(1)
                self.count_node[1] = node
                self._add_after(self.head, node)

            self.count_node[1].keys.add(key)

        else:
            cnt = self.key_count[key]
            nxt = cnt + 1
            self.key_count[key] = nxt

            cur_node = self.count_node[cnt]

            if nxt not in self.count_node:
                node = Node(nxt)
                self.count_node[nxt] = node
                self._add_after(cur_node, node)

            self.count_node[nxt].keys.add(key)

            cur_node.keys.remove(key)
            if not cur_node.keys:
                self._remove(cur_node)
                del self.count_node[cnt]

    def dec(self, key: str) -> None:
        cnt = self.key_count[key]
        cur_node = self.count_node[cnt]

        if cnt == 1:
            del self.key_count[key]
        else:
            prv = cnt - 1
            self.key_count[key] = prv

            if prv not in self.count_node:
                node = Node(prv)
                self.count_node[prv] = node
                self._add_after(cur_node.prev, node)

            self.count_node[prv].keys.add(key)

        cur_node.keys.remove(key)

        if not cur_node.keys:
            self._remove(cur_node)
            del self.count_node[cnt]

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))