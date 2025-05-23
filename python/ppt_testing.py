# Sample database as a dictionary where keys are usernames and values are passwords
database = {
    "john_doe": "secure123",
    "alice_smith": "password456",
    "bob_jones": "qwerty789"
}

# Function to check login credentials
def login(username, password):
    # Check if username exists in the database
    if username in database:
        # Check if password is correct
        if database[username] == password:
            return "Login Successful"
        else:
            return "Invalid Password"
    else:
        return "Username not found"

# Get user input for username and password
username_input = input("Enter username: ")
password_input = input("Enter password: ")

# Call the login function with user input
result = login(username_input, password_input)

# Output the result
print(result)
