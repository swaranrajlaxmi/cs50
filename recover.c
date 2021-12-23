#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;
 
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
        
        //initialise variables
        BYTE Buffer[512];
        int count = 0;
        char filename[8];
        FILE *outptr;
    
        //repeat until end of card
        while (fread(&Buffer, 512, 1, inptr) == 1)
        {
            // If start of a new JPEG 
            if (Buffer[0] == 0xff && Buffer[1] == 0xd8 && Buffer[2] == 0xff && (Buffer[3] & 0xf0) == 0xe0)
            {
                //close previous jpeg
                if (!(count == 0))
                {
                    fclose(outptr);
                }
                //name the file and open to write
                sprintf(filename, "%03i.jpg", count);
                outptr = fopen(filename, "w");
                count++;
            }
            // If JPEG has been found, write to file
            if (!(count == 0))
            {
                fwrite(&Buffer, 512, 1, outptr);
            }
        }
        fclose(inptr);
        fclose(outptr);
        return 0;
 
    }
}