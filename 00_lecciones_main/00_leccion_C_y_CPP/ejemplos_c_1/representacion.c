#include <stdio.h>

int main(void)
{
	// Declara y asigna valor a la variable a
	double var1, var2, var3, var4;
	var1 = 2./3; // 2./3 no tiene representacion finita ni en base decimal ni binaria
	var2 = 0.1; // 0.1 tiene representación finita en base decimal pero no en binaria
	var3 = 0.5; // 0.5 tiene representación finita en ambas bases

	// Muestra las variable por pantalla
	printf("var1 = %.20lf \n", var1); //%.20lf muestra un número de tipo double con 20 cifras decimales
	printf("var2 = %.20lf \n", var2);
	printf("var3 = %.20lf \n", var3);

	return 0;
}
