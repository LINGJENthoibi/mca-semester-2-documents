def is_even(n):
    return n % 2 == 0
n = int(input("Enter a number: "))
if is_even(n):
    print(n, "is even")
else:
    print(n, "is odd")

def greet_user(name):
    print(f"Hello, {name}!")
greet_user("Python")
