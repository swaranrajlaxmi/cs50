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
    //printing adjacent pyramids of hash
    for (int i = 0; i < height; i++)
    {
        //printing spaces in right alighned pyramid
        for (int j = 0; j < (height - (i + 1)); j++)
        {
           printf(" ");
        }
        //printing hash in right alighned pyrmid
        for (int k = 0; k < (i + 1); k++)
        {
            printf("#");
        }
        //printing gaps in adjacent pyramids
        printf("  ");
        //printing hash in left alighned pyramid
        for (int l = 0; l < (i + 1); l++)
        {
            printf("#");
        }
        printf("\n");       
                
    }
    
}