import math
import sympy as sp
print("Relation Calulation")
print("1. Quadratic Equation")
print("2. Cubic Equation")
print("3. Quartic Equation")
rel = input("Enter number of relation you want to calculate: ")

# quadratic root calculator
def quad():
    a = float(input("What is 'a': "))
    b = float(input("What is 'b': "))
    c = float(input("What is 'c': "))
    
    if a == 0:
        print("You're not dealing with a quadratic equation!")
        return
        
    D = b*b - 4.0*a*c 
    
    if D < 0:
        real_part = -b/(2*a)
        imag_part = math.sqrt(abs(D))/(2*a)
        print(f"Complex roots: {real_part}+{imag_part}i & {real_part}-{imag_part}i")
    else:
        x_1 = (-b + math.sqrt(D))/(2*a)
        x_2 = (-b - math.sqrt(D))/(2*a)
        print(f"The roots are {x_1} & {x_2}")

# cubic equation calculator
def cub():
    a = float(input("What is 'a': "))
    b = float(input("What is 'b': "))
    c = float(input("What is 'c': "))
    d = float(input("What is 'd': "))
    
    if a == 0:
        print("You're not dealing with a cubic equation!")
        return
    # Converting to depressed cubic form
    p = (3*a*c - b*b)/(3*a*a)
    q = (2*b*b*b - 9*a*b*c + 27*a*a*d)/(27*a*a*a)
    D = (q*q/4) + (p*p*p/27)
    
    if D > 0:
        u = math.cbrt(-q/2 + math.sqrt(D))
        v = math.cbrt(-q/2 - math.sqrt(D))  
        x_1 = u + v - b/(3*a)
        x_2 = -(u + v)/2 - b/(3*a) + complex(0, math.sqrt(3)/2)*(u - v)
        x_3 = -(u + v)/2 - b/(3*a) - complex(0, math.sqrt(3)/2)*(u - v) 
        print(f"One real root: {x_1}")
        print(f"Two complex roots: {x_2} & {x_3}")
    else:
        tea = math.acos(-q/(2*math.sqrt(-(p*p*p/27))))
        x_1 = 2*math.sqrt(-p/3)*math.cos(tea/3) - b/(3*a)
        x_2 = 2*math.sqrt(-p/3)*math.cos((tea + 2*math.pi)/3) - b/(3*a)
        x_3 = 2*math.sqrt(-p/3)*math.cos((tea + 4*math.pi)/3) - b/(3*a)  
        print(f"Three real roots are {x_1}, {x_2}, & {x_3}")

# Quartic root calculator with Newton's method
def quart():
    print("Solving quartic equation using Newton's method")
    a = float(input("What is 'a': "))
    b = float(input("What is 'b': "))
    c = float(input("What is 'c': "))
    d = float(input("What is 'd': "))
    e = float(input("What is 'e': "))
    x = sp.Symbol('x')
    equation = a*x**4 + b*x**3 + c*x**2 + d*x + e
    solutions = sp.solve(equation,x)
    print(f"The solutions are {solutions[0]}, {solutions[1]}, {solutions[2]} & {solutions[3]}")

if rel == "1":
    quad()
elif rel == "2":
    cub()
elif rel == "3":
    quart()
else:
    print("Invalid input")
