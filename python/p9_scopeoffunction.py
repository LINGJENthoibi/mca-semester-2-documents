def my_func():
    x = 10
    print("Inside function:", x)
my_func()
#print(x)

x = 5
def my_function():
    print("Acessing global x:", x)
my_func()
print("Outside function:", x)

x=100
def demo():
    x=50
    print("Inside function, x =", x)
demo()
print("Outside function, x =", x)
