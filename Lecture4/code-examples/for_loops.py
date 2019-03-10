names = ['Mario', 'Peter', 'Anna' ,'Paul' ,'Anna']

for number in range(2, 5):
    # In every iteration, we have a different value from iterable
    # We can access the value with the name we specified
    print(number)
    # range is collection of integers, we can use ints in indexing
    print('Hello', names[number])

    # Nested loops
    for name in names:
        # In every iteration name changes, in the order of names
        if name != names[number]:
            print(name, 'says hello to', names[number])