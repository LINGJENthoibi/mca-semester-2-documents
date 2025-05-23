#function 1
def greet():
    print("Hello, world")
greet()
#function 2
def greet(name):
    print(f"Hello, {name}")
greet("Alice")
#function 3
def add(c, d):
    return c + d
c = int(input("Enter first number: "))  
d = int(input("Enter second number: "))  
result = add(c, d)
print("The result is:", result)

#function 4
def greet(name="catch"):
    print(f"Hello, {name}!")
greet()
greet("Mike")
greet("Shone")
#function 5
def sum_numbers(*args): #*args helps to take multiple numbers
    return sum(args)
print(sum_numbers(10,20,30,40))
#lambda function6
add = lambda x,y,z:x+y+z
print(add(5, 6, 7))
