#include <stdio.h>


int main(void)
{
    int num_in, num_out, digit_in, digit_out, div;

    printf("Numero entrada: ");
    scanf("%d", &num_in);

    num_out = 0;
    div = 1;
    // Construye el número de salida dígito a digito
    while (num_in/div >= 1)
    {
        // Quita los números detrás del dígito de interés
        digit_in = (num_in / div)

        // Quita los números delante del dígito de interés
        digit_out = digit_in % 10; 

        // Escribe el dígito en el número de salida
        num_out += digit_in*div;

        // Pasa al siguiente dígito
        div *= 10;
    }

    printf("Número salida: %d\n", num_out);

    return 0;
}
