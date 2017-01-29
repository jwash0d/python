x = eval(input("Enter number between 0 and 1: "))
for i in range(10):
	x = 2.0 * x * (1-x)
	print(x)