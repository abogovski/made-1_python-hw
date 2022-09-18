from merge_without_duplicates import merge_without_duplicates


def test_should_merge_with_empty_iterables():
    assert merge_without_duplicates([], ()) == []
    assert merge_without_duplicates((-1, -1), []) == [-1]
    assert merge_without_duplicates((), [2, 2, 3]) == [2, 3]


def test_should_merge_without_duplicates():
    assert merge_without_duplicates(
        [-3, -3, -2, 4, 4, 4, 6],
        [-4, -3, -3, -3, -2, 6, 7]
    ) == [-4, -3, -2, 4, 6, 7]
