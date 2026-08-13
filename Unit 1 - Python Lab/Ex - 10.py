"""10.Write a program to demonstrate recursion using factorial or Fibonacci series."""

def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)


def get_fibonacci_term(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return get_fibonacci_term(n - 1) + get_fibonacci_term(n - 2)

if __name__ == "__main__":

    fact_num = 5
    fact_result = calculate_factorial(fact_num)
    print("\n1. Factorial Demonstration:")
    print("The factorial of",fact_num, "is: ",fact_result)

    fib_terms = 7
    print("\n2. Fibonacci Series Demonstration",fib_terms,"terms:")
    for i in range(fib_terms):
        print(get_fibonacci_term(i), end=" ")
    print()  
