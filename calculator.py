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

#result that will be returned
result = 0
# get user input
equation = raw_input("Enter a mathmatical equation:")
# split input into a list based on white space
equation_list = equation.split(" ")

# first handle simplest case: performing an operation on two numbers
x = int(equation_list[0])
y = int(equation_list[2])
operator = equation_list[1]
if operator == "+":
	result = add(x,y)
elif operator == "-":
	result = subtract(x,y)
elif operator == "*":
	result = multiply(x,y)
elif operator == "/":
	result = divide(x,y)

print(result)