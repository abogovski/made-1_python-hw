import math


def _all_close_to_zero(*nums, eps=1e-15):
    return all(math.isclose(num, 0, abs_tol=eps) for num in nums)


def solve_quadratic_equation(a, b, c, eps=1e-15):
    r'''
    Solves quadratic equation $a x^2 + b x + c = 0$.
    Returns:
        None, if there are no roots
        tuple with a single root, if two roots are less than `eps` apart
        tuple with two roots otherwise

    Raises:
        NotImplementedError, if $a \approx 0, b \approx 0, c \approx 0
    '''
    if _all_close_to_zero(a, b, c, eps=eps):
        raise NotImplementedError

    if _all_close_to_zero(a, b, eps=eps):
        return None

    if _all_close_to_zero(a, eps=eps):
        return - c / b,

    discriminant = b * b - 4 * a * c
    if _all_close_to_zero(discriminant, eps=eps):
        return - 0.5 * b / a,
    elif discriminant < 0:
        return None
    else:
        return (
            0.5 * (- b - math.sqrt(discriminant)) / a,
            0.5 * (- b + math.sqrt(discriminant)) / a,
        )
