# Programmer: Dalton Cole

def gcd(a, b):
	if a == b:
		return a
	if a > b:
		c = gcd(a - b, b)
	else:
		c = gcd(a, b - a)
	return c

print("Enter a: ")
first_input = input()
a = int(first_input)

print("Enter b: ")
second_input = input()
b = int(second_input)

print("The GCD of " + str(a) + " and " + str(b) + " is: " + str(gcd(a,b)))