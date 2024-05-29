import sys

x = int(input("x: "))
y = int(input("y: "))



try:
    result = x/y 
except ValueError:
    print("Error: Invalid Input")
    # exit the program 
    sys.exit(1)

try:
    result = x/y 
except ZeroDivisionError:
    print("Error: Canont divide by 0")
    # exit the program 
    sys.exit(1)



print(f"x/y = {result}")