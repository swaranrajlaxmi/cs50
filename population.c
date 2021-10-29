# include <stdio.h>
# include <cs50.h>
int main(void)
{

    int start_size, end_size, n = 0;
    //prompt the user for Start size untill the given condition is met
    do
    {
        start_size = get_int("Start size: ");
    }
    while (start_size < 9);
 
    //prompt the user for End size untill the given condition is met
    do
    {
        end_size = get_int("End size: ");
    }
    while (end_size < start_size);
 
    //calculate the number of years required for the population to reach at least the size of the end value.
    while (start_size < end_size)
    {
        start_size = start_size + start_size / 3 - start_size / 4;
        n++;
    }
    //print the number of years
    printf("Years: %d \n", n);
}