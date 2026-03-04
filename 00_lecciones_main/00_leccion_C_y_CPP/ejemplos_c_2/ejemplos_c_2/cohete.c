#include <math.h>

//**********************************************************************
// Este programa calcula la velocidad y altura de un proyectil
// lanzado verticalmente cierto tiempo T después del lanzamiento
// dada la altura inicial, velocidad y la aceleración de la gravedad.
//**********************************************************************

int main(void)
{
	double H0, H, V0, V, A, T;

	A = -9.8;
	H0 = 150.;
	V0 = 100.;
	T = 10.;

	H = 0.5*A*pow(T,2) + V0 + H0;
	V = A*T + V0;

	return 0;
}
