#Program to demonstrate creation of user defined function
def main():
    name = input("What is your name: ")
    hello(name)

def hello(name):
    print("Hello " + name)

main()