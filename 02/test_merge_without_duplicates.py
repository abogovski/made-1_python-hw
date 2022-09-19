from merge_without_duplicates import merge_without_duplicates


def test_should_filter_out_everything_for_empty_iterables():
    assert merge_without_duplicates([], ()) == []
    assert merge_without_duplicates((-1, -1), []) == []
    assert merge_without_duplicates((), range(3)) == []


def test_should_filter_out_everything_for_mutually_exclusive_numbers():
    assert merge_without_duplicates([0, 2], (1, 3)) == []
    assert merge_without_duplicates(range(2), [2, 3]) == []


def test_should_filter_unique_common_numbers_preserving_order():
    assert merge_without_duplicates(
        [1, 1, 2, 5, 7],
        (1, 1, 2, 3, 4, 7),
    ) == [1, 2, 7]
