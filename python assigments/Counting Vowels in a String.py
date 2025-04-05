n = input("Enter a string: ").lower()
vowels = "aeiou"
count = sum(1 for char in n if char in vowels)
print("Number of vowels:", count)
