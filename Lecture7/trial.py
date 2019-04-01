try:
    print(3/0)
except ZeroDivisionError as z:
    print("sorry", z)
else:
    print("else")
finally:
    print("finally")
