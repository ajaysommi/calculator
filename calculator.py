first_operand = float(input("Enter first operand: "))
second_operand = float(input("Enter second operand: "))
# defines variables for operands inputted by the user.

print("Calculator Menu")
print("---------------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division \n")
user_selection = int(input("Which operation do you want to perform? "))


# outputs menu for user to select a type of operation such as addition or subtraction.

# defines functions for arithmetic operations.
def addition():
    sum1 = first_operand + second_operand
    print(f"The result of the operation is {sum1}. Goodbye!")


def subtraction():
    difference = first_operand - second_operand
    print(f"The result of the operation is {difference}. Goodbye!")


def multiplication():
    product = first_operand * second_operand
    print(f"The result of the operation is {product}. Goodbye!")


def division():
    quotient = first_operand / second_operand
    print(f"The result of the operation is {quotient}. Goodbye!")


if user_selection == 1:
    addition()
elif user_selection == 2:
    subtraction()
elif user_selection == 3:
    multiplication()
elif user_selection == 4:
    division()
else:
    print("Error: Invalid selection! Terminating program.")
