#Fruitful function
def is_even(n):
    return n % 2 == 0
n = int(input("Enter a number: "))
if is_even(n):
    print(n, "is even")
else:
    print(n, "is odd")

#void function
def greet_user(name):
    print(f"Hello, {name}!")
greet_user("Python")

#function compose
def double(x):
    return x * 2
def square(x):
    return x * x
result = square(double(3))
print(result)

#Recursion
def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)
num = int(input("Enter any number:"))
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of" , num, "is",factorial(num))
