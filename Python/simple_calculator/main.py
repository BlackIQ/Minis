# It's a good practice to use Type Hint for args and return types, when you define functions like so:
# Python is a dynamic programming langugage which means you don'r need to specify the type of a variable
# in general it's a good way to be ensure about the type of a variable (type safety)
def divide(a: float, b: float) -> float:
    return a / b


def multiply(a: float, b: float) -> float:
    return a * b


def minus(a: float, b: float) -> float:
    return a - b


def sum(a: float, b: float) -> float:
    return a + b


if __name__ == "__main__":
    first_number = float(input("enter first number : "))
    seccond_number = float(input("enter seccond number: "))
    operator = input("enter operator (*-/+) : ")

    result = 0
    match operator:
        case "+":
            result = sum(first_number, seccond_number)
        case "-":
            result = minus(first_number, seccond_number)
        case "*":
            result = multiply(first_number, seccond_number)
        case "/":
            result = divide(first_number, seccond_number)

    print(result)
