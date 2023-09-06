def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Get input from the user
num = int(input("Enter a number: "))

result = factorial(num)
print("Factorial of", num, "is", result)