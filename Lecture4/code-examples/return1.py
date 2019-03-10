def factorial(n):
    result = 1
    if n == 0 or n == 1:
        return 1
        
    for i in range(1,n+1):
        result *= i
    return result
