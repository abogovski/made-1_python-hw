import operator
import pytest
from custom_list import CustomList


OPERAND_TYPES = [
    (list, CustomList),
    (CustomList, list),
    (CustomList, CustomList),
]


@pytest.fixture
def lists_to_compare():
    return {
        'left':          [1, 2, 3],      # sum: 6
        'right_less':    [1, 1, -1, 1],  # sum: 2
        'right_equal':   [5, -1, 2],     # sum: 6
        'right_greater': [10],           # sum: 10
    }


@pytest.mark.parametrize('left_type,right_type', OPERAND_TYPES)
@pytest.mark.parametrize('op,right_key,result', [
    (operator.gt, 'right_less',    True),
    (operator.gt, 'right_equal',   False),
    (operator.gt, 'right_greater', False),

    (operator.ge, 'right_less',    True),
    (operator.ge, 'right_equal',   True),
    (operator.ge, 'right_greater', False),

    (operator.eq, 'right_less',    False),
    (operator.eq, 'right_equal',   True),
    (operator.eq, 'right_greater', False),

    (operator.ne, 'right_less',    True),
    (operator.ne, 'right_equal',   False),
    (operator.ne, 'right_greater', True),

    (operator.le, 'right_less',    False),
    (operator.le, 'right_equal',   True),
    (operator.le, 'right_greater', True),

    (operator.lt, 'right_less',    False),
    (operator.lt, 'right_equal',   False),
    (operator.lt, 'right_greater', True),
])
def test_comparison(
    lists_to_compare,
    op, right_key, result,
    left_type, right_type
):
    left = left_type(list(lists_to_compare['left']))
    right = right_type(list(lists_to_compare[right_key]))

    assert op(left, right) == result

    assert list(left) == lists_to_compare['left']
    assert list(right) == lists_to_compare[right_key]


@pytest.mark.parametrize('left_type,right_type', OPERAND_TYPES)
@pytest.mark.parametrize('op', [operator.add, operator.sub])
def test_arithmetic(left_type, right_type, op):
    left = left_type([4, 1, 2, 3])
    right = right_type([3, 2, 1])

    result = op(left, right)
    assert type(result) == CustomList
    assert result == [op(4, 3), op(1, 2), op(2, 1), op(3, 0)]

    assert list(left) == [4, 1, 2, 3]
    assert list(right) == [3, 2, 1]


def test_str():
    assert str(CustomList([1, 2, 3])) == '[1, 2, 3] sum: 6'
