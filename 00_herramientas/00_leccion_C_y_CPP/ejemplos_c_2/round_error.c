#include <stdio.h>

int main(void)
{
	double var1, var2;
	int j;

	var1 = 0;
	var2 = 1e-7;

	for (j=0; j<1e9; j++)
	{
		var1 = var1 + var2;
	}

	printf("%lf \n", var1);

	return 0;
}
