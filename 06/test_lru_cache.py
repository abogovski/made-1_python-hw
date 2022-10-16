from lru_cache import LRUCache


def test_from_problem_statement():
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
