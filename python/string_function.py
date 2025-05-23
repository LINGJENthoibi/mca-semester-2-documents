#creating a string
text = "hello, python programming! "
print("Original string: ", text)

#1.Convert to lowercase
print("Lowercase: ", text.lower())


#1.Convert to uppercase
print("Uppercase: ", text.upper())

#3. Capitalize the first letter
print("Capitalize: ", text.capitalize())

#4.title function
print("Title Case:", text.title())

#5. swap case
print("Swap Case:", text.swapcase())

#6. Remove leading and trailing spaces
trimmed_text = text.strip()
print("Trimmed String:", trimmed_text)

#7. Check if string starts or end with
print("starts with 'Hello':", text.startswith("Hello"))
print("ends with 'Programming!':", text.endswith("Programming"))

#8. Find a substring
print("Index of 'python':", text.find("python"))

#9. Replace a substring
#new_text= text.replace("Python", "Java")
print("After Replace 'java' :", text.replace("python", "java"))

#10. Count occurance of a substring
print("count of 'o':", text.count("o"))

#11. Split a string into list
words = text.split()
print("Split int List:", words)

#12. Join list elements into a string
joined_text = "_".join(words)
print("Joined with '_':", joined_text)

#Check string properties
print("Is Alphabetic:", "Hello".isalpha())
print("Is digit:", "1234".isdigit())
print("Is Alphanumeric:", "Hello1234".isalnum())
print("Is Lower:", "hello".islower())
print("Is Upper:", "HELLO".isupper())
print("Is Title Case:", "Hello World".istitle())



