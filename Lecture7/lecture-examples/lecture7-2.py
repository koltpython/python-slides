try:
    a = float(input("Performance of CPUA:"))
    b = float(input("Performance of CPUA:"))
    performance_rate = a/b
except ZeroDivisionError:
    print("The second input cannot be zero!")
except ValueError as e:
    print(e)
else:
    print(performance_rate)

try:
    print(f'I have been living here for {years} years')
except NameError as e:
    print(e)

faculties = ["Case", "Ce", "Cs", "Ssch", "Med"]

while True:
    try:
        index = int(
            input(f'These are the faculties {faculties} which index do you want to use?'))
        faculties[index]
    except ValueError:
        print("index should be an integer")
    except IndexError as e:
        print(e)
    else:
        print(f'You chose {faculties[index]}')
        break

try:
    print(2 + '2')
except TypeError as e:
    print(e)
