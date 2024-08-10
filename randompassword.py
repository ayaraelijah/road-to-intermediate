import random
letters = ['A', 'B', 'C','D', 'E', 'a', 'b', 'c', 'd', 'e']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

nr_letters = input("How many letters do you want in your password: ")
nr_numbers = input("How many numbers do you want in your password: ")

password = ""
for char in range(1, nr_numbers + 1 ):
    password += char
    

for char in range(1, nr_letters + 1 ):
    password += char


print(password)
    
