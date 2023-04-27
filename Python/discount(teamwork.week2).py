from datetime import datetime

subtotal = float(input("Please enter the subtotal: "))

if subtotal <= 50:
    tax = subtotal * (6 / 100)
    total = subtotal + tax
    print(f"Sales tax amount: {tax: .2f}")
    print(f"Total: {total: .2f}")
    print()
elif subtotal >= 50:
    discount = subtotal * (10 / 100)
    t = subtotal - discount
    tax = t * (6 / 100)
    total = t + tax
    print(f"Discount amount: {discount: .2f}")
    print(f"Sales tax amount: {tax: .2f}")
    print(f"Total: {total: .2f}")
    print()
else:
    print()

