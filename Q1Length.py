# Read input from the user
user_input = input("Enter something: ")

# Count only the letters (ignoring numbers, spaces, and special characters)
letter_count = sum(1 for char in user_input if char.isalpha())

# Output the result
print(f"There are {letter_count} letters in your input.")