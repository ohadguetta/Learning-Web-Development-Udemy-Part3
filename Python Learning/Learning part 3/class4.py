# Challenge: Division by Zero

# Write a Python program that takes two numbers as input from the user and 
# # performs division operation on them. Your program should handle the division 
# by zero exception using a try-except block and display an appropriate error
#  message when division by zero occurs.

# Here's a template to get you started:

# python

def divide_numbers():
    try:
        # Get input from the user
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))

        # Perform division
        result = numerator / denominator

        # Print the result
        print("Result:", result)

    except ZeroDivisionError:
        # Handle division by zero exception
        print("Error: Division by zero is not allowed.")

divide_numbers()