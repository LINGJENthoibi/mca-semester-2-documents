print ("counting down from 5 to 20:")
count = 5
while count <= 20:
    print(count)
    count += 1
#break statement
print("Break example:")
for i in range(1, 11):
    if i == 10:
        print("Breaking the loop at", i)
        break
    print(i)

#continue statement
print("Continue example:")
for i in range(1, 15):
    if i == 7:
        print("Skipping", i)
        continue
    print(i)

#Precedence of operator
print("Precedence of opreator:")
x = 8 + 4 * 2
print(x)
y = (8 + 4) * 2
print(y)
z = 2 ** 4 ** 2
print(z)

#Input statement in python
name = input("Enter your name: ")
print("Hello", name, "!")

age = int(input("Enter your age: "))
print(f"You will be {age + 1} next year.")

price = float(input("Enter your price: "))
print(f"Total price with tax: {price * 1.1}")

name, age = input("Enter name and age: ").split()
print(f"Name: {name}, Age: {age}")

a, b, c = map(int, input("Enter Three numbers: ").split())
print(f"Sum: {a + b + c}")




#Output statement
print("Hello World")

name = "Alice"
age = 25
print("Name:", name, "Age:", age)
print("Hello ", "World", sep="-")
print("Python", end=" ")
print("Rocks!", end="\n")

name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old")




