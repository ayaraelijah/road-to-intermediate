import random
name = input("Enter your name: ")
print("Toss the coin\n")
random_code = random.randint(0,1)
if random_code == 1 :
 print(f"{name} you got Heads")
else:
 print(f"{name} you got Tails")