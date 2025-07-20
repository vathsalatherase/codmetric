##TASK 1

# Define functions for arithmetic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Start loop for repeated calculations
while True:
    try:
        # Take user input
        num1 = float(input("Enter first number: "))
        operator = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        # Perform calculation based on operator
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            # Handle division by zero
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = divide(num1, num2)
        else:
            print("Invalid operator. Use +, -, *, or /.")
            continue

        # Display result using f-string
        print(f"Result: {result:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except ZeroDivisionError as e:
        print(e)

    # Ask user if they want to continue
    again = input("Do you want to perform another calculation? (yes/no): ").lower()
    if again != 'yes':
        print("Thank you for using the calculator!")
        break

##OUTPUT# codmetric

<img width="561" height="238" alt="image" src="https://github.com/user-attachments/assets/38a42415-9838-4c8b-8aae-70e2ccc0e1a1" />
