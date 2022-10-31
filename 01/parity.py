def split_by_parity(collection):
    even, odd = [], []
    for num in collection:
        if not isinstance(num, int):
            raise ValueError(f'Got {num} with unexpected type{type(num)}')
        (odd if num & 1 else even).append(num)
    return even, odd
