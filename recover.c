#include <stdio.h>
#include <stdlib.h>
 
int main(int argc, char *argv[])
{
    //remind of correct usage
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }
    else
    // Open card.raw
    {
        FILE *inptr = fopen(argv[1], "r");
        
        if (inptr == NULL)
        {
            printf("cannot open %s\n", argv[1]);
            return 2;
        }
        
    }
 
}