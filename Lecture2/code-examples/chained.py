3 > 2 == 1 < 5 > 4  # => False
3 > (2 == 1) < 5 > 4  # => True
3 > True > False # => True
3 > 5 < 1/0  # => False
3 < 5 < 1/0  # => ZeroDivisionError