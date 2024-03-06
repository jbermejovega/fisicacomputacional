#include <stdio.h>

int main(void)
{
    int i;
    double vector[5];
    double suma;

    // Pide los valores por pantalla
    for (i=0; i< 5; i++)
    {
        printf("Valor %i: ", i);
        scanf("%lf", &vector[i]);
    }

    // Sume los valores
    suma = 0;
    for (i=0; i< 5; i++)
    {
         suma += vector[i];
    }

    printf("Suma = %lf\n", suma);

    return 0;
}
