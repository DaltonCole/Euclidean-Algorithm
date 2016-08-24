# Programmer: Dalton Cole

# Euclidean Algorithm: Given two integers a and b, a > b > 0
# a = q * b + r, 0 <= r < b
# GCD(a, b) = GCD(b, r)

import sys

print("Enter a: ")
first_input = input()
a = int(first_input)

print("Enter b: ")
second_input = input()
b = int(second_input)

# Make sure a is greater than b, if not, swap
if a < b:
	a, b = b, a

# a = q*b + r
q = a // b
r = a % b

# Show work if -s flag is passed
if "-s" in str(sys.argv):
	print("\n" + str(a) + " = " + str(q) + " * " + str(b) + " + " + str(r))


while r != 0:
	# Make b be the new a AND r be the new b
	a, b = b, r
	q = a // b
	r = a % b
	# Show work if -s flag is passed
	if "-s" in str(sys.argv):
		print(str(a) + " = " + str(q) + " * " + str(b) + " + " + str(r))

print("\nThe Greatest Common Divisor of " + first_input + " and " + second_input + " is: " + str(b))