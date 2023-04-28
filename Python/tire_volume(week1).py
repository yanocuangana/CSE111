import math

from datetime import datetime

width_of_the_tire = float(input("Enter the width of the tire in mm: "))
aspect_ratio_of_the_tire = float(input("Enter the aspect ratio of the tire: "))
diameter_of_the_wheel = float(input("Enter the diameter of the wheel in inches: "))
current_date_and_time = datetime.now()
som = width_of_the_tire * aspect_ratio_of_the_tire
som1 = 2540 * diameter_of_the_wheel
som2 = som + som1
volume = math.pi * width_of_the_tire**2 * aspect_ratio_of_the_tire * som2 / 10000000000
print(f"The approximate volume is {volume: .2f} liters.")
print(current_date_and_time)

with open("tire_volume(week1).txt","at") as python:
    print(width_of_the_tire, aspect_ratio_of_the_tire, diameter_of_the_wheel, volume, current_date_and_time, file = python)

