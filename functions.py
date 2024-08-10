def paint_calc(height, width, coverage):
    num_of_cans = (height * width) / coverage
    return round(num_of_cans)

height = int(input("Enter the height: "))
width = int(input("Enter the width: "))
coverage = 5

result = paint_calc(height, width, coverage)

print(f"You'll need {result} cans of paint ")