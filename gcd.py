# Programmer: Dalton Cole

def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)
		
print("Enter a: ")
first_input = input()
a = int(first_input)

print("Enter b: ")
second_input = input()
b = int(second_input)

if a > b:
	a, b = b, a

print("The GCD of " + str(a) + " and " + str(b) + " is: " + str(gcd(a,b)))