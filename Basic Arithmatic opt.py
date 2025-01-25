def get_valid_input(prompt):
    """Function to handle input validation dynamically."""
    while True:
        try:
            # Ask the user for input
            return int(input(prompt))  # Return valid integer input
        except ValueError:
            print("Invalid input! Please enter a valid number.")
           # retry = input("Do you want to try again? (yes/no): ").strip().lower()
            #if retry != "yes":
             #   print("Exiting the program.")
            #exit()

# Main Calculator Logic
print("Welcome to the Dynamic Calculator!")

# Use the dynamic function to get valid inputs
num1 = get_valid_input("Enter the first number: ")
num2 = get_valid_input("Enter the second number: ")

# Perform operations
print(f"The sum of {num1} and {num2} is {num1 + num2}.")
print(f"The difference of {num1} and {num2} is {num1 - num2}.")
print(f"The product of {num1} and {num2} is {num1 * num2}.")

try:
    print(f"The division of {num1} by {num2} is {num1 / num2}.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
