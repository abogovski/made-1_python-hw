def get_closest_to_zero(nums_list):
    '''
    Receives list of integers.
    Filters integers closest to zero.
    '''
    if nums_list:
        min_dist = min(abs(num) for num in nums_list)
    return [num for num in nums_list if abs(num) == min_dist]
