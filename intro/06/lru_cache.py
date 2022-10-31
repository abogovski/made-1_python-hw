from ordered_dict import OrderedDict


class LRUCache:
    def __init__(self, cache_size):
        self._cache_size = cache_size
        self._ordered_dict = OrderedDict()

    def __len__(self):
        return len(self._ordered_dict)

    def get(self, key):
        value = self._ordered_dict.extract(key)
        if value is None:
            return None

        self._ordered_dict.add(key, value)
        return value

    def set(self, key, value):
        self._ordered_dict.extract(key)
        self._ordered_dict.add(key, value)
        if len(self._ordered_dict) > self._cache_size:
            oldest_key = self._ordered_dict.oldest_key()
            self._ordered_dict.extract(oldest_key)
