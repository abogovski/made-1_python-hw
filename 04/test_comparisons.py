import pytest
from custom_list import CustomList


@pytest.fixture
def lists():
    return {
        'left':          [1, 2, 3],
        'right_less':    [1, 1, -1, 1],
        'right_equal':   [5, -1, 2],
        'right_greater': [10],
    }


@pytest.mark.parametrize('right_type', [list, CustomList])
def test_gt_comparison(right_type, lists):
    assert CustomList(lists['left']) > right_type(lists['right_less'])
    assert not CustomList(lists['left']) > right_type(lists['right_equal'])
    assert not CustomList(lists['left']) > right_type(lists['right_greater'])


@pytest.mark.parametrize('right_type', [list, CustomList])
def test_ge_comparison(right_type, lists):
    assert CustomList(lists['left']) >= right_type(lists['right_less'])
    assert CustomList(lists['left']) >= right_type(lists['right_equal'])
    assert not CustomList(lists['left']) >= right_type(lists['right_greater'])


@pytest.mark.parametrize('right_type', [list, CustomList])
def test_eq_comparison(right_type, lists):
    assert not CustomList(lists['left']) == right_type(lists['right_less'])
    assert CustomList(lists['left']) == right_type(lists['right_equal'])
    assert not CustomList(lists['left']) == right_type(lists['right_greater'])


@pytest.mark.parametrize('right_type', [list, CustomList])
def test_ne_comparison(right_type, lists):
    assert CustomList(lists['left']) != right_type(lists['right_less'])
    assert not CustomList(lists['left']) != right_type(lists['right_equal'])
    assert CustomList(lists['left']) != right_type(lists['right_greater'])


@pytest.mark.parametrize('right_type', [list, CustomList])
def test_le_comparison(right_type, lists):
    assert not CustomList(lists['left']) <= right_type(lists['right_less'])
    assert CustomList(lists['left']) <= right_type(lists['right_equal'])
    assert CustomList(lists['left']) <= right_type(lists['right_greater'])


@pytest.mark.parametrize('right_type', [list, CustomList])
def test_lt_comparison(right_type, lists):
    assert not CustomList(lists['left']) < right_type(lists['right_less'])
    assert not CustomList(lists['left']) < right_type(lists['right_equal'])
    assert CustomList(lists['left']) < right_type(lists['right_greater'])
