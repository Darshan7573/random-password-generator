import random
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to password Generator")
nr_letters=int(input("How many letters would to like to have in your password\n"))
nr_numbers=int(input("How many numbers would to like to have in your password\n"))
nr_symbols=int(input("How many symbols would to like to have in your password\n"))
password=""
for char in range (1,nr_letters +1):
	password =  password + random.choice(letters)
for char in range (1,nr_numbers +1):
	password = password + random.choice(numbers)
for char in range (1,nr_symbols+1):
	password = password + random.choice(numbers)
print(f"Your password is {password}")
