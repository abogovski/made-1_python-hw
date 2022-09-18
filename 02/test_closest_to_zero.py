from closest_to_zero import get_closest_to_zero


def test_should_get_closest_to_zero_for_trivial_cases():
    assert get_closest_to_zero([]) == []
    assert get_closest_to_zero([1]) == [1]
    assert get_closest_to_zero([-1]) == [-1]


def test_should_get_single_closest_to_zero_num():
    assert get_closest_to_zero([11, -10, -13, 12, 11]) == [-10]
    assert get_closest_to_zero([-11, 10, 13, -12, -11]) == [10]


def test_should_get_multiple_closest_to_zero_nums():
    assert get_closest_to_zero(
        [-12, -11, 12, 11, -11, 13, -14]
    ) == [-11, 11, -11]
