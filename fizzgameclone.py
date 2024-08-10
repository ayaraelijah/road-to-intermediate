#get input of range from user
name = input("Enter your name: ")
print(f"{name} welcome to fizzbuzz game ")
for number in range(1, int(input("Enter the number you want the listing to end\n")) + 1) :
 if number % 3== 0:
  print("Fizz")
 elif number % 5 == 0:
  print("Buzz")
 elif number % 3 == 0 and number % 5 == 0:
  print("FizzBuzz")
 else:
  print(number)
