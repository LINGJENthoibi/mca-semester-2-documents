def add(a, b):
    return a + b

def sub(c, d):
    return c - d

def mul(e, f):
    return e * f

def div(g, h):
    return g / h

x = int(input("Enter first number: "))  
y = int(input("Enter second number: "))  

add1 = add(x, y)
sub1 = sub(x, y)
mul1 = mul(x, y)
div1 = div(x, y)

print("Addition:", add1)
print("Subtraction:", sub1)
print("Multiplication:", mul1)
print("Division:", div1)
