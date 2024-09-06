#Program to demonstrate use of try, except
def main():
    num = get_int("Enter a number: ")
    print(f"The number entered is {num}")

def get_int(prompt):
    while True:
        try:
            num = int(input(prompt))
        except ValueError:
            #pass
            print("The input should be integer")
        else:
            return num

main()