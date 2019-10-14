def my_max(*nums):
    """Returns the maximum of the given arguments.
    Returns -infinity if no arguments are given."""  
    max_num = -float('inf')
    for n in nums:
        if n > max_num:
            max_num = n
    return max_num