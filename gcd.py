# Code from: https://codility.com/media/train/10-Gcd.pdf

def gcd(a, b, res):
	if a == b:
		return res * a
	elif (a % 2 == 0) and (b % 2 == 0):
		return gcd(a // 2, b // 2, 2 * res)
	elif (a % 2 == 0):
		return gcd(a // 2, b, res)
	elif (b % 2 == 0):
		return gcd(a, b // 2, res)
	elif a > b:
		return gcd(a - b, b, res)
	else:
		return gcd(a, b - a, res)

print("Enter a: ")
first_input = input()
a = int(first_input)

print("Enter b: ")
second_input = input()
b = int(second_input)

print("\nThe Greatest Common Divisor of " + first_input + " and " + second_input + " is: " + str(gcd(a, b, 1)))