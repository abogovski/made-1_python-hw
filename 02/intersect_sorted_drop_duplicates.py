def merge(left_iterable, right_iterable):
    '''
    Filters common elements from two sorted iterables.
    Removes duplicates from result.
    '''
    result = []
    left_iter, right_iter = iter(left_iterable), iter(right_iterable)

    try:
        left, right = next(left_iter), next(right_iter)
        while True:
            if left == right and (not result or result[-1] != left):
                result.append(left)
            if left <= right:
                left = next(left_iter)
            if right < left:
                right = next(right_iter)

    except StopIteration:
        pass

    return result
