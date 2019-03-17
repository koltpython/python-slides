biology = {'Ashley', 'Patrick', 'Molly', 'Bob',
           'Mark', 'Matt'}
calculus = {'Becca', 'Shira', 'Alex', 'Molly', 'Bob', 'Steph'}
spanish = {'Matt', 'Mark', 'Bob', 'Alex', 'Steph', 'Julia', 'Andy'}
# intersection &
print(biology.intersection(calculus))  # => {'Molly', 'Bob'}
print(calculus & spanish)  # => {'Bob', 'Alex', 'Steph'}
# union |
print(biology.union(calculus))  # => all names except andy and julia
print(calculus | spanish | biology)  # => all names
# difference -
print((biology - calculus).intersection(spanish))  # => {'Mark', 'Matt'}
# symmetric_difference ^
print(biology.symmetric_difference(spanish))
# => {'Molly', 'Julia', 'Ashley', 'Alex', 'Steph', 'Andy', 'Patrick'}
