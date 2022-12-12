# Ask the user for the first number
num1 = input("Enter the first number: ")

# Ask the user for the second number
num2 = input("Enter the second number: ")

# Convert the input strings to numbers
num1 = float(num1)
num2 = float(num2)

# Ask the user for the operation to perform
operation = input("Enter the operation to perform (+, -, *, /): ")

# Perform the operation
if operation == "+":
  result = num1 + num2
elif operation == "-":
  result = num1 - num2
elif operation == "*":
  result = num1 * num2
elif operation == "/":
  result = num1 / num2
else:
  print("Invalid operator")

# Print the result
print("The result is:", result)

# made by KingTreemox aka Treemox