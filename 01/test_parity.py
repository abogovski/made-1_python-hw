from parity import split_by_parity
import pytest


def test_should_split_by_parity():
    assert split_by_parity([]) == ([], [])
    assert split_by_parity([-2, 4, 2]) == ([-2, 4, 2], [])
    assert split_by_parity([-1, 3, 1]) == ([], [-1, 3, 1])
    assert split_by_parity([-12345678, 23456789, 567, 345678, -123456789]) == (
        [-12345678, 345678],
        [23456789, 567, -123456789]
    )


def test_should_raise_error_if_num_type_is_not_int():
    with pytest.raises(ValueError):
        split_by_parity([1, -2.])
