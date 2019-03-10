def factorial(n):
    result = 1
    if n == 0 or n == 1:
        print(1)
    else:
        for i in range(1,n+1):
            result *= i
        print(result)

factorial(0) # => 1
factorial(1) # => 1
factorial(3) # => 6
factorial(4) # => 24
factorial(5) # => 120

