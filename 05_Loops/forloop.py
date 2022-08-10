# Python program to illustrate
# Iterating over a list
l = ["geeks", "for", "geeks"]
for i in l:
	print(i)

# Prints all letters except 'e' and 's'
for letter in 'geeksforgeeks':
	if letter == 'e' or letter == 's':
		continue
	print('Current Letter :', letter)

# Break Statement in Python_______________________________________
for letter in 'geeksforgeeks':

	# break the loop as soon it sees 'e'
	# or 's'
	if letter == 'e' or letter == 's':
		break

print('Current Letter :', letter)

# range() function in Python _______________________________________________

# Python Program to
# show range() basics

# printing a number
for i in range(10):
	print(i, end=" ")

# performing sum of first 10 numbers
sum = 0
for i in range(1, 10):
	sum = sum + i
print("\nSum of first 10 numbers :", sum)
