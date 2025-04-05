# Basic String Manipulation
message = "Hello, World!"
print(message)

text = "Python Programming"
first_five = text[:5]
print(first_five)

# String Methods
string1 = "python is fun"
uppercase_string = string1.upper()
print(uppercase_string)

string2 = "Python is fun"
replaced_string = string2.replace("fun", "awesome")
print(replaced_string)

# String Formatting
name = "John"
age = 25
formatted_message = f"My name is {name}, and I am {age} years old."
print(formatted_message)

price = 49.99
formatted_price = f"{price:.2f}"
print(formatted_price)

# String Functions
sentence = "Hello, how are you?"
o_count = sentence.count('o')
print(o_count)

sentence2 = "Hello, world! Python is amazing."
position = sentence2.find("world")
print(position)

# Reverse and Check
reverse_python = "Python"[::-1]
print(reverse_python)

word = "madam"
is_palindrome = word == word[::-1]
print(is_palindrome)
