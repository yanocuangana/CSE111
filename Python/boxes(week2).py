import math
number1 = int(input("Enter the number of items: "))
number2 = int(input("Enter the number of items per box: "))
boxes = math.ceil(number1 / number2)
print(f"For {number1} items, packing {number2} items in each box, you will need {boxes} boxes.")