# arithmatic functions

def add(x, y):
   """This function adds two numbers"""
   return x + y

def subtract(x, y):
   """This function subtracts two numbers"""
   return x - y

def multiply(x, y):
   """This function multiplies two numbers"""
   return x * y

def divide(x, y):
   """This function divides two numbers"""
   return x / y

def calc(equation):	
	# split input into a list based on white space
	equation_list = equation.split(" ")

	#result that will be returned
	result = 0

	# perform a series of operations on the full arithmetic expression
	x = int(equation_list.pop(0))
	while len(equation_list) > 0:
		operator = equation_list.pop(0)
		y = int(equation_list.pop(0))
		
		if operator == "+":
			result = add(x,y)
		elif operator == "-":
			result = subtract(x,y)
		elif operator == "*":
			result = multiply(x,y)
		elif operator == "/":
			result = divide(x,y)

		# reset x to be the current result for use in the next round of operations
		x = result

	return result

# get user input
equation = raw_input("Enter a mathmatical equation:")
output = calc(equation)
print(output)