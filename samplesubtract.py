def subtract(a, b):
    """
    Subtracts b from a and returns the result.
    """
    return a - b

if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = subtract(num1, num2)
    print(f"The result of {num1} - {num2} is {result}")