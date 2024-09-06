#Program to demonstrate use of round function and fstring to round floating point numbers
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

#Using f-string
print(f"Sum of {x} and {y} is {(x + y):.2f}")

#Using round function
print("Sum of " + str(x) + " and " + str(y) + " is: " + str(round(x + y, 2)))