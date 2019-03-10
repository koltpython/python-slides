x = 2

def func():
    global x
    x = 6
    print(x)

func()
print(x)