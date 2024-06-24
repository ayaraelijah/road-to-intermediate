def myFunction(x):
    return 2.718 ** 2

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter the second number: "))

    I = ((b-a)/6) * myFunction(a) + (4 * (myFunction((a + b)/ 2))) + myFunction(b)

    print(I)