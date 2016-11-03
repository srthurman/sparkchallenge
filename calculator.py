# arithmetic functions

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


# find the appropriate arithmetic function to use
def pemdas(equation_list, operand):
	temp_list = list(equation_list)
	operand_in_list = operand in temp_list
	operand_func = {
		"*": multiply,
		"/": divide,
		"+": add,
		"-": subtract
	}
	while operand_in_list:
		if operand in temp_list:
			operand_index = temp_list.index(operand)
			x_index = operand_index - 1
			y_index = operand_index + 1
			x = int(temp_list[x_index])
			y = int(temp_list[y_index])
			operator_result = operand_func[operand](x,y)
			temp_list[x_index] = operator_result
			temp_list.pop(y_index)
			temp_list.pop(operand_index)
		else:
			operand_in_list = False
	return temp_list

#main logic
def calc(equation):	
	#result that will be returned
	result = 0

	# split input into a list based on white space
	equation_list = equation.split(" ")

	# look for arithmetic operations in PEMDAS order
	equation_list = pemdas(equation_list, "*")
	equation_list = pemdas(equation_list, "/")
	equation_list = pemdas(equation_list, "+")
	equation_list = pemdas(equation_list, "-")

	result = equation_list[0]
	return result

if __name__ == "__main__":
	# get user input
	equation = raw_input("Enter a mathmatical equation:")
	output = calc(equation)
	print(output)