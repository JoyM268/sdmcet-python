#Program to demonstrate returning of value from a user defined function
def main():
    x = int(input("Enter the number: "))
    print(f"The square of {x} is {square(x)}")

def square(n):
    return n ** 2

main()