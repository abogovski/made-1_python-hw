from lru_cache import LRUCache


def test_single_value_cache():
    cache = LRUCache(1)

    cache.set('k1', 'val1')
    assert len(cache) == 1
    assert cache.get('k1') == 'val1'

    cache.set('k2', 'val2')
    assert len(cache) == 1
    assert cache.get('k1') is None
    assert cache.get('k2') == 'val2'


def test_two_values_cache():
    cache = LRUCache(2)

    cache.set('k1', 'val1')
    assert len(cache) == 1

    cache.set('k2', 'val2')
    assert len(cache) == 2

    assert cache.get('k3') is None
    assert cache.get('k2') == 'val2'
    assert cache.get('k1') == 'val1'

    cache.set('k3', 'val3')
    assert len(cache) == 2

    assert cache.get('k3') == 'val3'
    assert cache.get('k2') is None
    assert cache.get('k1') == 'val1'


def test_set_for_existing_key():
    cache = LRUCache(2)

    cache.set('k1', 'val1.1')
    cache.set('k2', 'val2')
    assert len(cache) == 2
    assert cache.get('k1') == 'val1.1'

    cache.set('k1', 'val1.2')
    assert len(cache) == 2

    cache.set('k3', 'val3')
    assert len(cache) == 2
    assert cache.get('k1') == 'val1.2'
    assert cache.get('k2') is None
    assert cache.get('k3') == 'val3'
