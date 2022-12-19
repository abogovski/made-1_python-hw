import pytest


def test_from_str():
    assert int('-3') == -3
    assert int('9' * 100) == 10 ** 100 - 1
    assert int('3h', 18) == 71
    with pytest.raises(ValueError):
        int('3h', 17)


def test_aritmetic_ops():
    assert int(-126) + int(250) == 124
    assert int(2) * int(-3) == -6
    assert int(-2) ** int(3) == -8
    assert int(7) // int(2) == 3


def test_bit_ops():
    assert int(0b11) | int(0b101) == int(0b111)
    assert int(0b11) & int(0b101) == int(0b1)
    assert int(0b11) ^ int(0b101) == int(0b110)


def test_bit_methods():
    assert int(127).bit_length() == 7
    assert int(128).bit_length() == 8
    assert int(-127).bit_length() == 7
    assert int(-128).bit_length() == 8
