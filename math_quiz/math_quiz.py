import random


def random_integer(min, max):
    """
    Generates a random integer between min & max and returns it.

    Parameters:
    - min (int): The minimum integer value.
    - max (int): The maximum integer value.

    Returns:
    int: The random integer between min and max.
    """

    return random.randint(min, max)


def random_operator():
    """
    Returns:
    string: One of the random operator + , - or *

    """
    return random.choice(['+', '-', '*'])


def math_operation(num_1, num_2, operator):
    """
    Returns the math problem statement and its solution.

    Parameters:
    - num_1 (int): First operand integer value.
    - num_2 (int): Second operand integer value.
    - operator (string): The mathematical operator

    Returns:
    string: The mathematical problem statement
    int: The solution
    """

    problem = f"{num_1} {operator} {num_2}"
    if operator == '-':
        answer = num_1 - num_2
    elif operator == '+':
        answer = num_1 + num_2
    else:
        answer = num_1 * num_2
    return problem, answer


def math_quiz():
    s = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(int(t_q)):
        num_1 = random_integer(1, 10)
        num_2 = random_integer(1, 5)
        o = random_operator()

        PROBLEM, ANSWER = math_operation(num_1, num_2, o)
        print(f"\nQuestion: {PROBLEM}")
        try:
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)
        except ValueError:
            print("Invalid input!.\n")

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")


if __name__ == "__main__":
    math_quiz()
