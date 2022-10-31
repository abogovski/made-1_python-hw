import logging
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
            logging.warning('key "%s" miss', key)
            return None

        logging.info('key "%s" hit: "%s"', key, value)
        self._ordered_dict.add(key, value)
        return value

    def set(self, key, value):
        logging.info('set value "%s" for key "%s"', value, key)
        self._ordered_dict.extract(key)
        self._ordered_dict.add(key, value)
        if len(self._ordered_dict) > self._cache_size:
            oldest_key = self._ordered_dict.oldest_key()
            logging.warning('cache size violation => forget oldest key "%s"', oldest_key)
            self._ordered_dict.extract(oldest_key)
