#n = float ( input ( "Digite um número: " ))
#r = round(n)
#print(r)


import math

# Get a number from the user.
number = float(input("Enter a number: "))
root = math.sqrt(number)
print(f"The square root is {root:.2f}")
if root < 100:
    print(f"The square root is less than 100.")
elif root > 100:
    print(f"The square root is more than 100.")
else:
    print(f"The square root is exactly 100.")