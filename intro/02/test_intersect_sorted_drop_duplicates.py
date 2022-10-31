from intersect_sorted_drop_duplicates import merge


def test_should_filter_out_everything_for_empty_iterables():
    assert merge([], ()) == []
    assert merge((-1, -1), []) == []
    assert merge((), range(3)) == []


def test_should_filter_out_everything_for_mutually_exclusive_numbers():
    assert merge([0, 2], (1, 3)) == []
    assert merge(range(2), [2, 3]) == []


def test_should_filter_unique_common_numbers_preserving_order():
    assert merge([1, 1, 2, 5, 7], (1, 1, 2, 3, 4, 7)) == [1, 2, 7]
