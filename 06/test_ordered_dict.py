from ordered_dict import OrderedDict


def test_empty_ordered_dict():
    ordered_dict = OrderedDict()
    assert len(ordered_dict) == 0
    assert ordered_dict.oldest_key() is None
    assert ordered_dict.extract('key') is None


def test_single_value_ordered_dict():
    ordered_dict = OrderedDict()
    ordered_dict.add('k1', 'v1')
    assert len(ordered_dict) == 1
    assert ordered_dict.oldest_key() == 'k1'

    assert ordered_dict.extract('k1') == 'v1'
    assert len(ordered_dict) == 0
    assert ordered_dict.extract('k1') is None


def test_multiple_values_ordered_dict():
    ordered_dict = OrderedDict()
    ordered_dict.add('k1', 'v1')
    ordered_dict.add('k2', 'v2')
    ordered_dict.add('k3', 'v3')
    ordered_dict.add('k4', 'v4')
    assert len(ordered_dict) == 4
    assert ordered_dict.oldest_key() == 'k1'
    assert ordered_dict.extract('k5') is None

    assert ordered_dict.extract('k3') == 'v3'
    assert len(ordered_dict) == 3
    assert ordered_dict.oldest_key() == 'k1'
    assert ordered_dict.extract('k3') is None

    assert ordered_dict.extract('k1') == 'v1'
    assert len(ordered_dict) == 2
    assert ordered_dict.oldest_key() == 'k2'
    assert ordered_dict.extract('k1') is None

    ordered_dict.add('k5', 'v5')
    assert len(ordered_dict) == 3
    assert ordered_dict.oldest_key() == 'k2'

    assert ordered_dict.extract('k5') == 'v5'
    assert len(ordered_dict) == 2
    assert ordered_dict.oldest_key() == 'k2'
    assert ordered_dict.extract('k5') is None
