def product(*nums, scale = 1):
    p = scale
    for n in nums:
        p *= n
    return p