# include <stdio.h>
# include <cs50.h>
# include <math.h>

int main(void)
{
    float dollar;
    //prompt user for change owed
    do
    {
        dollar = get_float("change owed: ");
    }
    while (dollar <= 0);
    //converting the user’s inputted dollars to cents
    int cents = round(dollar * 100);
    int coins = 0;

    while (cents >= 1)
    {
        if (cents >= 25)
        {
            cents = cents - 25;
            coins++;
        }
        else if (cents >= 10)
        {
            cents = cents - 10;
            coins++;
        }
        else if (cents >= 5)
        {
            cents = cents - 5;
            coins++;
        }
        else if (cents >= 1)
        {
            cents = cents - 1;
            coins++;
        }
    }
    printf("%i\n", coins);


}
