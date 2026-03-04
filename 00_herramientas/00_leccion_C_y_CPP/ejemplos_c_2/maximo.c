#include <stdio.h>

int main(void)
{
    int i;
    int num;

    num = 1;

    for (i=0; i<40; i++)
    {
        num = num*2;
        printf("%e\n", (double) num);
    }

    return 0;
}
