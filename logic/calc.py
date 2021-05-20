def calculate(operator1, operation, operator2):
    if operation == '+':
        return operator1 + operator2
    elif operation == '-':
        return operator1 - operator2
    elif operation == '*':
        return operator1 * operator2
    else:
        return operator1 / operator2
