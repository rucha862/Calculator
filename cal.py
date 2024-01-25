# Function to add two numbers
def add(x, y):
    return x + y


# Function to subtract two numbers
def subtract(x, y):
    return x - y


# Copy first snippet here


# Main program loop
while True:
    # Display menu
   print("Options:")
   print("Enter 'add' for addition")
   print("Enter 'subtract' for subtraction")
    # Copy second snippet here
   print("Enter 'quit' to end the program")


    # User input
    user_input = input(": ")


    # Check if user wants to quit
    if user_input == "quit":
        break


    # Check for valid operation
    if user_input in ("add", "subtract"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))


        if user_input == "add":
           print("Result:", add(num1, num2))
        elif user_input == "subtract":
           print("Result:", subtract(num1, num2))
        # Copy fourth snippet here     
    else:
       print("Invalid input")