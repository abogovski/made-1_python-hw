import pytest
from quadratic_equation import solve_quadratic_equation


def _allclose_tuples(result, cannonical):
    return (
        isinstance(result, tuple) and
        len(result) == len(cannonical) and
        all(
            got == pytest.approx(expected)
            for got, expected in zip(result, cannonical)
        )
    )


def test_should_return_tuple_with_both_roots_of_quadratic_equation():
    assert _allclose_tuples(solve_quadratic_equation(2, 4, -30), (-5, 3))


def test_should_return_single_root_tuple_for_quadratic_equation():
    assert _allclose_tuples(solve_quadratic_equation(1, -2, 1), (1, ))
    assert _allclose_tuples(
        solve_quadratic_equation(1 - 1e-18, -2, 1 + 1e-16),
        (1, )
    )


def test_should_return_none_for_quadratic_equation_with_no_roots():
    assert solve_quadratic_equation(1, -1, 1) is None


def test_should_solve_linear_equation():
    assert _allclose_tuples(solve_quadratic_equation(0, 4, -10), (2.5, ))
    assert _allclose_tuples(solve_quadratic_equation(-1e-16, 2, 3), (-1.5, ))


def test_should_return_none_for_inconsistent_equation_of_constants():
    assert solve_quadratic_equation(0, 0, 1) is None
    assert solve_quadratic_equation(1e-16, 1e-16, -1e-14) is None


def test_should_raise_not_implemented_for_consistent_equation_of_constants():
    with pytest.raises(NotImplementedError):
        solve_quadratic_equation(0, 0, 0)

    with pytest.raises(NotImplementedError):
        solve_quadratic_equation(1e-16, -1e-16, 1e-16)
