import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))

nr_symbols = int(input(f"How many symbols would you like?\n"))

nr_numbers = int(input(f"How many numbers would you like?\n"))

print("Here is your password: ", end='')
number_letter = 0
for temp_letters in letters:
    if number_letter < nr_letters:
        picked_letters = random.choice(letters)
        number_letter += 1
        print(picked_letters, end='')

number_symbols = 0
for temp_symbols in symbols:
    if number_symbols < nr_symbols:
        picked_symbols = random.choice(symbols)
        number_symbols += 1
        print(picked_symbols, end='')

number_number = 0
for temp_number in numbers:
    if number_number < nr_numbers:
        picked_numbers = random.choice(numbers)
        number_number += 1
        print(picked_numbers, end='')
