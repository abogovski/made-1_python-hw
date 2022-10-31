class KeyValueListNode:
    def __init__(self, key=None, value=None, prev_node=None, next_node=None):
        self.key = key
        self.value = value
        self.prev = prev_node
        self.next = next_node


class OrderedDict:
    def __init__(self):
        self._first = KeyValueListNode()
        self._last = KeyValueListNode(prev_node=self._first)
        self._first.next = self._last
        self._key_to_node = {}

    def __len__(self):
        return len(self._key_to_node)

    def oldest_key(self):
        return self._first.next.key

    def extract(self, key):
        node = self._key_to_node.get(key)
        if node is None:
            return None

        node.prev.next = node.next
        node.next.prev = node.prev
        del self._key_to_node[key]
        return node.value

    def add(self, key, value):
        assert key not in self._key_to_node and value is not None
        node = KeyValueListNode(key, value, self._last.prev, self._last)
        node.prev.next = node
        node.next.prev = node
        self._key_to_node[key] = node
