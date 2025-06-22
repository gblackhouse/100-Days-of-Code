from art import logo
print(logo)
calculating = True
n1 = float(input("Type the first number\n"))
while calculating:
    operation = input("Choose the operation\n")
    n2 = float(input("Type the second number\n"))


    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b
    def multiply(a, b):
        return a * b
    def divide(a, b):
        return a / b

    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
    }

    calculator = operations[operation]
    answer = calculator(n1,n2)
    print(answer)

    continue_calculating = input("Do you want to continue? y/n")
    if continue_calculating == 'yes':
        n1 = answer
    elif continue_calculating == 'no':
        print("\n" * 100)
        n1 = float(input("Type the first number\n"))







