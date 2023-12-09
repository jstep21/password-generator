import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Input amount of letters, symbols, and numbers for password to have
nr_letters = random.randint(20, 30)
nr_symbols = random.randint(5, 10)
nr_numbers = random.randint(5, 10)

password_list = []

# Generate random letters
for char in range(nr_letters):
    password_list.append(random.choice(letters))
# Generate random symbols    
for char in range(nr_symbols):
    password_list += random.choice(symbols)
# Generate random numbers
for char in range(nr_numbers):
    password_list += random.choice(numbers)

# Shuffle and add to password
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
