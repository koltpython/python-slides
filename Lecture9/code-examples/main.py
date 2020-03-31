import custom_math as math

if __name__ == "__main__":
    a = int(input("Please enter a number: "))
    b = int(input("Please enter a number: "))
    c = input("Please enter one of the following operations: sum, substraction, multiplication, division: ")

    if c == "sum":
        print(math.sum(a, b))
    elif c == "substraction":
        print(math.substraction(a, b))
    elif c == "multiplication":
        print(math.multiplication(a, b))
    else:
        print(math.division(a, b))