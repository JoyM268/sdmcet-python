#Program to print a square of given number of rows
def main():
    rows = int(input("Enter the number of rows: "))
    print_square(rows)

def print_square(rows):
    for i in range(rows):
        for j in range(rows):
            print("#", end="")
        print()

main()