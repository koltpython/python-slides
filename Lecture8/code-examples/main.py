import area_calculator

#import custom_math
#import custom_math as math
#from custom_math import summation, substraction
#from custom_math import *
#from custom_math import substraction as subs

def area_calculation():

    shape = input("Please enter the shape to be calculated: ")

    if shape == "circle":
        radius = int(input("Please enter the radius of circle: "))
        pi = area_calculator.pi
        print(area_calculator.area_circle(pi, radius))    

    elif shape == "triangle":
        base = int(input("Please enter the base length of triangle: "))
        height = int(input("Please enter the height of triangle: "))

        print(area_calculator.area_triangle(base, height))

    elif shape == "rectangle":
        width = int(input("Please enter the width of rectangle: "))
        height = int(input("Please enter the height of rectangle: "))

        print(area_calculator.area_rectangle(width, height))

    else:
        print("The shape you entered is not defined.")


if __name__ == "__main__":
    
    area_calculation()

    #a = int(input("Please enter a number: "))
    #b = int(input("Please enter a number: "))
    
    #print(custom_math.summation(a, b))
    #print(custom_math.substraction(a, b))
    #print(custom_math.multiplication(a, b))
    #print(custom_math.division(a, b))

    #print(math.summation(a, b))
    #print(math.substraction(a, b))
    #print(math.multiplication(a, b))
    #print(math.division(a, b))
    
    #print(summation(a, b))
    #print(substraction(a, b))

    #print(summation(a, b))
    #print(substraction(a, b))
    #print(multiplication(a, b))
    #print(division(a, b))

    #print(subs(a, b))
