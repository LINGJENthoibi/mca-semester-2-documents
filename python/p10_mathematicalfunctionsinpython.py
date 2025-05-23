import math
x = float(input("Enter a number (x):"))
y = float(input("Enter another number (y):"))
print("\n--- Built in functions ---")
print("Absolute value of x:", abs(x))
print("x raised to the power y:", pow(x, y))

print("Minimun of x and y:", min(x, y))
          
print("Maximun of x and y:", max(x, y))
print("Round x to 2 decimal places:", round(x, 2))
          
print("\n--- Math Module Functions ----")
print("Square rooth of x:", math.sqrt(abs(x)))
print("Ceiling of x:", math.ceil(x))
print("Floor of x:", math.floor(x))

#Factorial only accepts integer >= 0
if x >= 0 and x.is_integer():
          print("Factorial of int(x):", math.factorial(int(x)))
else:
    print("Factorial: Not define for negative or non integer x")
          

#Logarithms
if x > 0:
    print("Natural log of x:", math.log(x))
    print("Log base 10 of x:", math.log10(x))
    print("e raised to power x:", math.exp(x))
else:
    print("Logs: Not defined for non-positive x")
print("\n--- Trigonometric functions (in radians) ---")
print("Sine of x:", math.sin(x))
print("Cosine of x:", math.cos(x))
print("tangent of x:", math.tan(x))

print("\n--- Constants ---")
print("Value of pi:", math.pi)
