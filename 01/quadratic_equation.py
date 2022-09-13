import math


EPS = 1e-15


def solve_quadratic_equation(a, b, c):
    '''
    Solves quadratic equation $a x^2 + b x + c = 0$.

    Returns:
        None, if there are no roots
        tuple with a single root, if two roots are less than `EPS` apart
        tuple with two roots otherwise

    Raises:
        ValueError for degenerate quadratic equations
    '''
    if math.isclose(a, 0, abs_tol=EPS):
        raise ValueError('Equation is not quadratic')

    discriminant = b*b - 4*a*c

    if discriminant <= -EPS:
        return None
    if discriminant < EPS:
        return -0.5 * b / a,

    return (
        -0.5 * (b + math.sqrt(discriminant)) / a,
        -0.5 * (b - math.sqrt(discriminant)) / a,
    )
