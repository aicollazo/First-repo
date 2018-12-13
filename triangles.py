from math import sqrt
def hypotenuse(a,b):
    a = float(input("a: "))
    b = float(input("b: "))
    c = sqrt(a**2 + b**2)
    print(f"The hypotenuse is {c}")
