# required argument missing
info()
# non-keyword argument after a keyword argument
info(num = 2, 'Jane')
# duplicate value for the same argument
info(2, num = 3)
# unknown keyword argument
info(person = 'Jane')