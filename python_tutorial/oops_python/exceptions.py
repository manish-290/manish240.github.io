import sys

try:
    a = int(input("num1:"))
    b= int(input("num2:"))
except  ValueError:
    print("Invalid input")
    sys.exit(1)

try:
    result = a/b
except  ZeroDivisionError:
    print("Error:Cannot divide by zero")
    sys.exit(1)
    
print(result)