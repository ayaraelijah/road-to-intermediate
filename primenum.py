def prime_checker(n):
    is_prime = True
    for num in range(2, n):
      if n % num == 0:
         is_prime = False
    if is_prime:
       print(f"it is a prime number")
    
    else:
       print(f"it is not a prime number")
n = int(input("Input a number in the range from 1 to 100: "))

prime_checker(n)