def interpreter ():
    expression = input("Expression: ")
    x, operator, z = expression.split(" ")

    x = int(x)
    z = int(z)
    result = calculateExpression(x, operator , z)
    print(f"Result: {result:.1f}")

def calculateExpression(x, operator, z):
    if operator == "+":
        return x + z
    elif operator == "-":
        return x - z
    elif operator == "*":
        return x * z
    elif operator == "/":
        if z != 0:
            return x / z
        else:
            return "Cannot divide by 0"
    else:
        return "Invalid operator"

interpreter()
