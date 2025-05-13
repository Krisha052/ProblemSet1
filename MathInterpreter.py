
def main():
    expression = input("Expression: ")
    print(calculator(expression))

def calculator(expression):
    x, y, z = expression.split(" ")
    x, z = float(x), float(z)
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "/":
        return x / z
    elif y == "*":
        return x * z

if __name__ == "__main__":
    main()