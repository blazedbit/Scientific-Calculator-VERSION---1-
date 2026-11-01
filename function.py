# FUNCTIONS DEFINED HERE
import math

def addition():
    total = 0
    try:
        var = int(input("Enter the number of values you want to add: "))
        if var <= 0:
            print("Error: Number of values must be greater than zero.")
            return
        for i in range(var):
            num = float(input("Enter number: "))
            total += num
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    except EOFError:
        print("Error: Unexpected end of input.")
        return
    return total

def subtraction():
    try:
        var = int(input("Enter the number of values you want to subtract: "))
        if var <= 0:
            print("Error: Number of values must be greater than zero.")
            return
        num1 = float(input("Enter the first number: "))
        for i in range(var - 1):
            num2 = float(input("Enter number: "))
            num1 -= num2
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    except EOFError:
        print("Error: Unexpected end of input.")
        return
    return num1

def multiplication():
    product = 1
    try:
        var = int(input("Enter the number of values you want to multiply: "))
        if var <= 0:
            print("Error: Number of values must be greater than zero.")
            return
        for i in range(var):
            num = float(input("Enter number: "))
            product *= num
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    except EOFError:
        print("Error: Unexpected end of input.")
        return
    return product

def division():
    try:
        var = int(input("Enter the number of values you want to divide: "))
        if var <= 0:
            print("Error: Number of values must be greater than zero.")
            return
        num1 = float(input("Enter the first number: "))
        for i in range(var - 1):
            num2 = float(input("Enter number: "))
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            num1 /= num2
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    except EOFError:
        print("Error: Unexpected end of input.")
        return
    return num1

def square_root():
    try:
        num = float(input("Enter a number to find its square root: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    except EOFError:
        print("Error: Unexpected end of input.")
        return
    if num < 0:
        print("Error: Cannot compute the square root of a negative number.")
        return
    result = math.sqrt(num)
    return result

def power():
    try:
        base = float(input("Enter the base number: "))
        exponent = float(input("Enter the exponent: "))
        if base == 0 and exponent <= 0:
            print("Error: 0 raised to a non-positive exponent is undefined.")
            return
        if base < 0 and not exponent.is_integer():
            print("Error: Negative base with a non-integer exponent is not allowed.")
            return
        result = math.pow(base, exponent)
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    except EOFError:
        print("Error: Unexpected end of input.")
        return
    except OverflowError:
        print("Error: The result is too large to compute.")
        return
    return result

def logarithm():
    try:
        num = float(input("Enter a number to find its logarithm: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    except EOFError:
        print("Error: Unexpected end of input.")
        return
    if num <= 0:
        print("Error: Logarithm is not defined for non-positive numbers.")
        return 
    result = math.log(num)
    return result

def sine():
    try:
        angle = float(input("Enter an angle in degrees to find its sine: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    except EOFError:
        print("Error: Unexpected end of input.")
        return
    radians = math.radians(angle)
    result = math.sin(radians)
    return result

def cosine():
    try:
        angle = float(input("Enter an angle in degrees to find its cosine: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    except EOFError:
        print("Error: Unexpected end of input.")
        return
    radians = math.radians(angle)
    result = math.cos(radians)
    return result

def tangent():
    try:
        angle = float(input("Enter an angle in degrees to find its tangent: "))
        if (angle % 180) == 90:
            print("Error: Tangent is undefined for angles of 90 + k*180 degrees.")
            return
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    except EOFError:
        print("Error: Unexpected end of input.")
        return
    radians = math.radians(angle)
    result = math.tan(radians)
    return result

def factorial():
    try:
        num = int(input("Enter a non-negative integer to find its factorial: "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        return
    except EOFError:
        print("Error: Unexpected end of input.")
        return
    if num < 0:
        print("Error: Factorial is not defined for negative numbers.")
        return
    result = math.factorial(num)
    return result

def absolute_value():
    try:
        num = float(input("Enter a number to find its absolute value: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    except EOFError:
        print("Error: Unexpected end of input.")
        return
    result = abs(num)
    return result

def percentage():
    try:
        num = float(input("Enter the number: "))
        percent = float(input("Enter the percentage: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    except EOFError:
        print("Error: Unexpected end of input.")
        return
        
    result = (num * percent) / 100
    return result

def modulo():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    except EOFError:
        print("Error: Unexpected end of input.")
        return
    if num2 == 0:
        print("Error: Modulo by zero is not allowed.")
        return
    result = num1 % num2
    return result

def multiple_operations():
    numlist = []
    operators = []
    try:
        expression = input("Enter the expression (e.g., 2+3*4): ")
    except EOFError:
        print("Error: Unexpected end of input.")
        return
    if expression.strip()    == "":
        print("Error: Expression cannot be empty.")
        return
    char = 0
    while char < len(expression):
        if expression[char].isdigit() or expression[char] == '.' or expression[char] == '-' and (char == 0 or expression[char - 1] in ['+', '-', '*', '/', '%']):
            num = ''
            if expression[char-1] == ' ' and expression[char] == '-':
                num += '-'
                char += 1
            if expression[char] == '-':
                num += '-'
                char += 1
            while char < len(expression) and (expression[char].isdigit() or expression[char] == '.'):
                num += expression[char]
                char += 1
            try:
                float(num)
                numlist.append(num)
            except ValueError:
                print(f"Error: Invalid number '{num}' in the expression.")
                return
        elif expression[char] in ['+', '-', '*', '/', '%']:
            operators.append(expression[char])
            char += 1

        elif expression[char] == ' ':
            char += 1

        else:
            print(f"Error: Invali   d character '{expression[char]}' in the expression.")
            return

    if len(numlist) == 0:
        print("Error: No numbers found in the expression.")
        return
    if len(operators) == 0:
        print("Error: No operators found in the expression.")
        return
    if len(numlist) - 1 != len(operators):
        print("Error: Mismatch between numbers and operators.")
        return
    
    i = 0

    while i < len(operators):
        if operators[i] in ['*', '/', '%']:
            a = float(numlist[i])
            b = float(numlist[i + 1])

            if operators[i] in ['/', '%'] and b == 0:
                print("Error: Division or modulo by zero is not allowed.")
                return

            if operators[i] == '*':
                result = a * b
            elif operators[i] == '/':
                result = a / b
            else:
                result = a % b

            numlist[i] = str(result)
            del numlist[i + 1]
            del operators[i]
        else:
            i += 1

    result = float(numlist[0])

    for i in range(len(operators)):
        if operators[i] == '+':
            result += float(numlist[i + 1])
        elif operators[i] == '-':
            result -= float(numlist[i + 1])

    return result
     
