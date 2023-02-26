import random

def arithmetic_captcha():
    """Generates an arithmetic captcha question and returns the solution."""
    # Generate two random integers between 0 and 10
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)

    # Generate a random arithmetic operator (+, -, or *)
    operator = random.choice(['+', '-', '*'])

    # Create the captcha question
    question = f"What is {num1} {operator} {num2}?"

    # Calculate the solution
    if operator == '+':
        solution = num1 + num2
    elif operator == '-':
        solution = num1 - num2
    else:
        solution = num1 * num2

    return question, solution
arithmetic_captcha()
