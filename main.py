def polish_notation (operator, operand1, operand2):
    """
    Арифметические действия
    """
    if operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        result = operand1 / operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '+':
        result = operand1 + operand2
    else:
        pass
    return result

def main():
    user_command = input()
    operator, operand1, operand2 = (c for c in user_command if c != ' ')
    print(operator, operand1, operand2)

main()

