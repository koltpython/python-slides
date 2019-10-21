x = 10 # => global

def func():
    x = 5 # => local
    y = 7 # => local
    print(x, y) 

func()
print(x)