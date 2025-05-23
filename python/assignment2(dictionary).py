# 1. Creating a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
print(student)

# 2. Accessing dictionary values
print(student["grade"])

# 3. Counting frequency of characters in a string
text = "banana"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print(freq)

# 4. Representing JSON using dictionary
person = {
    "name": "Bob",
    "location": {"city": "Paris", "country": "France"},
    "skills": ["Python", "Data Analysis"]
}
print(person)

# 5. Replacing switch case using dictionary
def add(x, y): return x + y
def subtract(x, y): return x - y

operations = {
    "add": add,
    "subtract": subtract
}
print(operations["add"](10, 5))
print(operations["subtract"](10, 5))

# 6. Storing configuration
config = {
    "theme": "dark",
    "autosave": True,
    "timeout": 300
}
print(config)

# 7. Data from database example
employee = {
    "id": 101,
    "name": "John",
    "department": "HR"
}
print(employee)

# Extended program for Dictionary
student = {"name": "John", "age": 18, "grade": "A"}
print("Name:", student.get("name"))
print("Age:", student["age"])

student["marks"] = 90
student["age"] = 19
student.pop("grade")

for key, value in student.items():
    print(key, ":", value)
