// **************************************************
// EJEMPLO DE ASIGNACIÓN DINÁMICA DE MEMORIA EN C
// **************************************************

// La biblioteca stdlib contiene las funciones malloc y free, necesarias
// para asignar y liberar memoria dinámicamente
#include <stdlib.h>
#include <stdio.h> // Necesario para pedir valores y escribir por pantalla

int main(void)
{
    int n_elementos; // Nº de elementos en el vector
    int i; // Contador

    // Para crear un vector dinámico, tenemos que declarar un puntero en el
    // que se almacenará la dirección de la memoria asignada dinámicamente
    double* vector;

    // Preguntamos por pantalla el número de elementos del vector
    printf("Nº elementos: ");
    scanf("%i", &n_elementos);

    // Asignamos la memoria necesaria para almacenar el número de variables
    // de tipo double indicado por n_elementos.
    // Para ello usamos la función malloc.
    // La función malloc toma como argumento la cantidad de memoria que hay
    // que asignar, en nuestro caso n_elementos veces el tamaño de un double,
    // y devuelve la dirección de memoria del primer elemento
    vector = malloc(n_elementos*sizeof(double));
    // En C++, el comando sería: vector = new double[n_elementos];

    // Ya podemos usar la variable vector como un array cualquiera 
    // Ejemplo sencillo: calcular y almacenar los primeros n_elementos
    // números pares
    for (i=0; i<n_elementos;i++)
    {
        vector[i] = (i+1)*2;
    }
    // Mostramos ahora estos números
    for (i=0; i<n_elementos;i++)
    {
        printf("%lf\n", vector[i]);
    }

    // Una vez hayamos terminado de usar el vector, podemos liberar la
    // memoria que ocupa con la función free
    free(vector);
    // En C++, el comando sería: delete[] vector;

    return 0;
}
