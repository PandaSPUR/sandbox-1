#include <stdio.h>

main()
{
	int fib[2] = {0, 1};
	int fibnum, fib_temp;

	printf("The first 10 Fibonacci numbers are:\n");
	printf("0\n");
	printf("1\n");

	for(fibnum = 3; fibnum < 11; fibnum++)
	{
		fib_temp = fib[0] + fib[1];
		fib[0] = fib[1];
		fib[1] = fib_temp;

		printf("%i\n", fib_temp);
	}

	return 0;
}

		
