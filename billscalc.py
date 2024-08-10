print("Welcome to bills calculator")
bill = int(input("What was the bill?\n#"))
tip = int(input("How much tip did you give\n#"))
people = int(input("How many people were you with?\n"))
total_bill = bill + tip 
total_bill_shared_people = total_bill / people
print(f"the bill for each person is {total_bill_shared_people}")



