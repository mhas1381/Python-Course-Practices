def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What is the first number: "))
    for operation in operations:
        print(operation)
    is_continue = True

    while is_continue:
        num2 = float(input("What is the next number: "))

        operation_symbol = input("Pick an operation: ")

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f'{num1} {operation_symbol} {num2} = {answer}')
        user_choice = input("Do you want to continue[Y] or start a new calculation[N]:").lower()
        if user_choice == "y":
            num1 = answer
        else:
            is_continue = False
            calculator()

calculator()