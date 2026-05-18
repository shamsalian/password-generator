import secrets
import string

print("===== PASSWORD GENERATOR =====")

# Ask user preferences
length = int(input("Enter password length: "))

include_lowercase = input("Include lowercase letters? (y/n): ").lower()
include_uppercase = input("Include uppercase letters? (y/n): ").lower()
include_numbers = input("Include numbers? (y/n): ").lower()
include_symbols = input("Include symbols? (y/n): ").lower()

# Store selected characters
characters = ""

if include_lowercase == "y":
    characters += string.ascii_lowercase

if include_uppercase == "y":
    characters += string.ascii_uppercase

if include_numbers == "y":
    characters += string.digits

if include_symbols == "y":
    characters += string.punctuation

# Check if user selected at least one option
if characters == "":
    print("Error: You must select at least one character type.")
else:
    # Generate password
    password = ""

    for i in range(length):
        password += secrets.choice(characters)

    print("\nGenerated Password:")
    print(password)