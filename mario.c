# include <stdio.h>
# include <cs50.h>

int main()
{
    int height;
    //prompt the user for height untill the given condition is met
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);
    //
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < height; j++)
        {
            if (j < height - (i + 1))
            {
                printf(" ");
            }
            else
            {
               printf("#"); 
            }
        }
        printf("\n");       
                
    }
    
}