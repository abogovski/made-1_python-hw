import pytest
from custom_list import CustomList


@pytest.mark.parametrize(
    'left_type,right_type',
    [
        (CustomList, CustomList),
        (CustomList, list),
        (list, CustomList),
    ],
)
def test_add(left_type, right_type):
    result = left_type([1, 2, 3, 4]) + right_type([2, 3, 4])
    assert type(result) == CustomList
    assert result == [1 + 2, 2 + 3, 3 + 4, 4 + 0]


@pytest.mark.parametrize(
    'left_type,right_type',
    [
        (CustomList, CustomList),
        (CustomList, list),
        (list, CustomList),
    ],
)
def test_subtract(left_type, right_type):
    result = left_type([1, 2, 3]) - right_type([4, 3, 2, 1])
    assert type(result) == CustomList
    assert result == [1 - 4, 2 - 3, 3 - 2, 0 - 1]


def test_str():
    assert str(CustomList([1, 2, 3])) == '[1, 2, 3] sum: 6'
