import math

width = float(input("Enter the width of the tire in mm: "))
rat = float(input("Enter the aspect ratio of the tire: "))
diam = float(input("Enter the diameter of the wheel in inches: "))
som = width * rat
som1 = 2540 * diam 
som2 = som + som1
volume = math.pi * width**2 * rat * som2 / 10000000000
print(f"The approximate volume is {volume: .2f} liters.")
