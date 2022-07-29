from art import logo


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
    "/": divide,
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)

    wants_to_continue = True
    while wants_to_continue:

        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What's the next number?: "))

        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        continuation_input = input(
            f"Type 'y' to continue calculating with {answer}, type 'n' to start over or type 'e' to exit:").lower()
        if continuation_input == "y":
            num1 = answer
        elif continuation_input == "n":
            calculator()
        else:
            wants_to_continue = False


calculator()
