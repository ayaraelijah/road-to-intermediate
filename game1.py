import random
user_choice = int(input("Enter your choice. Type 0 for Rock, Type 1 for paper, Type 2 for scissors\n"))

computer_choice = random.randint(0,2)
print(f"Computer chose {computer_choice}\n\n")

if user_choice >= 3 or user_choice < 0:
    print("invalid number")
elif user_choice == 0 and computer_choice == 2:
    print("you win")
elif computer_choice == 0 and user_choice == 2:
    print("you lose")
elif computer_choice > user_choice:
    print("you lose")
elif user_choice > computer_choice:
    print("You win")
elif computer_choice == user_choice:
    print("Draw")

