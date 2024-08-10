print("Welcome to the True love calculator\n")
name1 = input("Enter your name: ")
name2 = input("Enter your partner name: ")

combined_name = name1 + name2
combined_names = combined_name.lower()

t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")

first_part = t + r + u + e

l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")

second_part = l + o + v + e

lovescore = int(str(first_part) + str(second_part))

if lovescore < 10 and lovescore > 90:
    print(f"Your score is {lovescore}, you are lovebirds")
elif lovescore >= 40 & lovescore <= 50:
    print(f"your score is {lovescore}, you are alright together")
else:
    print(f"your score is {lovescore}")