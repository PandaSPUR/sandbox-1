sandbox
=======

<<<<<<< HEAD
AppSec-13-Assignment-1
=======
AppSec Sandbox
>>>>>>> 91aea7713960700a70a86f7a355f2416ecf033f1

Author: Dominic Spinosa
Class: Application Security (Fall 2013)
Instructor: Justin Cappos
FInal Modified Date: 9/17/13

Turing-Complete Sandbox
---------------------------------------
Functionality and Purpose:

	This application reads in a Python script line-by-line and executes each
	line separately while comparing called functions against a determined
	whitelist, which act as a "safe" subset of the Python language. This whitelist
	is enforced by removing all other functions from the local built-in function
	list, thus rendering any functions that do not reside within the whitelist
	as undefined/prohibited. This sandbox supports calculations and mathematical
	operations within the provided (input) program and also supports inherent
	Python output (preceded by an string of "ERROR:"). The stack and incurred
	data types are memory-restricted as well to avoid potential overflow
	vulnerabilities.

Environment:

	This application has been tested and is able to execute within the confines
	of an Ubuntu 12.X OS platform (specifically, a VM).

Required Files:
	
	"sandbox.py" Python script
	user's Python script(s)

Execution (from the command line):

	python sandbox.py <Python script>

Examples:

	Example Python scripts have been provided within the GitHub repository
	in order to demonstrate the execution of this sandbox application. These
	example scripts are as follows:

		counting.py
		fibonacci.py


