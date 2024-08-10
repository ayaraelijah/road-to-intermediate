import random

word_list = ["Baboon", "impossible", "psychology"]

ran_choice = random.choice(word_list).lower()
word_length = len(ran_choice)

end_of_game = False
lives = 6

display = []
for _ in range(word_length):
   display += "_"
print(display)

while not end_of_game:
   guess = input("Guess a letter: ").lower()
   
   if guess in display:
      print(f"you have already guessed the letter {guess}")

   for position in range(word_length) :
      letter = ran_choice[position]
      
      if letter == guess :
         display[position] = letter
   

   if guess not in ran_choice:
      print(f"you guessed {guess} that is not in the word, you lose a life")
   
      lives -= 1
      if lives == 0:
         end_of_game = True
         print("You lose")

   print(f"{''.join(display)}")
     
   if "_" not in display:
      end_of_game = True
      print("You win")
