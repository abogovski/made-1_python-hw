from pytest import (
    approx,
    mark,
    raises,
)
from quadratic_equation import (
    EPS,
    solve_quadratic_equation as solve,
)


def test_should_return_tuple_with_both_roots_of_quadratic_equation():
    assert solve(2, 4, -30) == (approx(-5), approx(3))


def test_should_return_single_root_tuple_for_quadratic_equation():
    assert solve(1, -2, 1) == (approx(1), )
    assert solve(1 - EPS/100, -2, 1 + EPS/10) == (approx(1), )


def test_should_return_none_for_quadratic_equation_with_no_roots():
    assert solve(1, -1, 1) is None


@mark.parametrize('eps', [-EPS, -EPS/2, 0, EPS/2, EPS])
def test_should_raise_value_error_for_degenerate_quadratic_equations(eps):
    with raises(ValueError):
        solve(eps, 4, -10)

    with raises(ValueError):
        solve(eps, -eps, 1)

    with raises(ValueError):
        solve(eps, 0, 0)
