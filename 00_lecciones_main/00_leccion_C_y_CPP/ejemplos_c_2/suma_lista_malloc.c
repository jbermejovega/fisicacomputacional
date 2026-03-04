#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int i;
    int n;
    double *vector;
    double suma;

    // Pide el número de elementos a sumar
    printf("Nº de elementos:");
    scanf("%i", &n);

    // Asigna la memoria al vector
    vector = (double*) malloc(n * sizeof(double));

    // Pide los valores por pantalla
    for (i=0; i<n; i++)
    {
        printf("Valor %i: ", i);
        scanf("%lf", &vector[i]);
    }

    // Sume los valores
    suma = 0;
    for (i=0; i<n; i++)
    {
         suma += vector[i];
    }

    printf("Suma = %lf\n", suma);

    free(vector);

    return 0;
}
