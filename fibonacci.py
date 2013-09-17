#///////////////////////////////////////////////////////////////
#
#	Dominic Spinosa
#	Application Security
#	Assignment 1 - Turing Complete Sandbox
#	Test Case 2
#	9/12/13
#
#	This program calculates and outputs the first ten 
#	numbers of the Fibonacci sequence.
#
#///////////////////////////////////////////////////////////////

fib = [0, 1]
fibnum, fib_temp

print("The first 10 Fibonacci numbers are: ")
print("0")
print("1")

for fibnum in range(3, 11):
	fib_temp = fib[0] + fib[1]
	fib[0] = fib[1]
	fib[1] = fib_temp

	print(fib_temp)

