def __append_if_not_duplicate(result, value):
    if not result or result[-1] != value:
        result.append(value)


def __flush_tail(result, tail):
    for value in tail:
        __append_if_not_duplicate(result, value)


def merge_without_duplicates(left, right):
    '''
    Merges two sorted collections of ints into a list.
    Removes duplicates.
    '''
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            __append_if_not_duplicate(result, left[left_idx])
            left_idx += 1
        else:
            __append_if_not_duplicate(result, right[right_idx])
            right_idx += 1

    __flush_tail(result, left[left_idx:])
    __flush_tail(result, right[right_idx:])

    return result
