#define calculating functions
def add(n1, n2) :
	return n1 + n2

def subtract(n1, n2) :
	return n1 - n2

def multiply(n1, n2) :
	return n1 * n2

def divide(n1, n2) :
	return n1 / n2

def modulus(n1, n2) :
	return n1  % n2


# request an operation from user

print("Select a method of operation: ")
operator = input()

# request a number from a user
print("Enter a number: ")
firstNumber = int(input())

# request a second number from user
print("Enter another number: ")
secondNumber = int(input())

# calculate the 2 numbers using the operator user requested
if operator == '+' :
	result = add(firstNumber, secondNumber)

elif operator == '-' :
	result = subtract(firstNumber, secondNumber)

elif operator == '*' :
	result = multiply(firstNumber, secondNumber)

elif operator == '/' :
	result = divide(firstNumber, secondNumber)

elif operator == '%' :
	result = modulus(firstNumber, secondNumber)

else:
	result = "invalid"

# print result
print(str(firstNumber) + ' ' + operator + ' ' + str(secondNumber) + ' = ' + str(result))