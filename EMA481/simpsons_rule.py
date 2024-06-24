#Numerical analysis Simpsons rule
def myFunction(x):
    return 2.718 ** 2

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

I = ((b-a)/6) * myFunction(a) + (4 * (myFunction((a + b)/ 2))) + myFunction(b)

print(I)