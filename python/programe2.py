
#creating
fruits = ("Apple", "Banana", "Cherry", "Orange")
print("Tuple fruits:", fruits)

#accessing elements
print("First fruits:", fruits[0])
print("Last fruits:", fruits[-1])

#packaging and unpakaging
person =("Alice", 25, "New York")
name, age, city = person
print("name:", name)
print("age:", age)
print("city:", city)

#nested tuple
nested_tuple = (1,(2,3),(4,5,6))
print("Nested tuple:", nested_tuple)
print("Accessing nested value:", nested_tuple[1][1])

#finding length
print("First two fruits:", fruits[:2])
print("Number of fruits:", len(fruits))

#counting
numbers = (1,2,2,3,4,2,5)
print("Count of 2:", numbers.count(2))

#finding index
print("Index of fruits:", fruits.index("Cherry"))

#slicing
print("Slicing:", fruits[:2])

