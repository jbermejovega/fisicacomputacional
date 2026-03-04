#include <stdio.h>

int main(void)
{
	// Declara las variables
	int n1, n2;

	// Asigna valor a las variables 
	n1 = 1;
	n2 = 2;

	// Muestra diferentes divisiones
	printf("3/2 = ");
	printf("%i", 3/2);
	printf("\n");
	
	printf("3./2 = ");
    printf("%lf", 3./2);
	printf("\n");

	printf("3/2. = ");
	printf("%lf", 3/2.);
	printf("\n");

	printf("3./2. = ");
	printf("%lf", 3./2.);
	printf("\n");
	
	printf("n1/n2 = ");
	printf("%i", n1/n2);	
	printf("\n");

	return 0;
}
