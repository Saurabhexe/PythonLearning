# A simple Python function

def fun(text):
    print("Welcome to GFG")

# A simple Python function
def fun():
	print("Welcome to GFG")


# Driver code to call a function
fun()
# _________________________________________________

def add(num1: int, num2: int) -> int:
	"""Add two numbers"""
	num3 = num1 + num2

	return num3

# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")

