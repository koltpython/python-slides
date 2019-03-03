x = 1
while x < 100:
    x *= 2
    if (x+1) % 3 == 0:
        break
    print(x)
