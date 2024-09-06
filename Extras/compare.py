#Program to compare two numbers
x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))
if x < y:
    print(f"{x} is less than {y}")
elif x > y:
    print(f"{x} is greater than {y}")
else:
    print("Both the numbers are equal")