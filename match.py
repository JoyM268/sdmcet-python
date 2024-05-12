#Program to demonstrate use of match
num = int(input("Enter 1, 2 or 3: "))
match num:
    case 1:
        print("One was entered")
    case 2:
        print("Two was entered")
    case 3:
        print("Three was entered")
    case _:
        print("Invalid input")