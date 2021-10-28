# include <stdio.h>
# include <cs50.h>
int main(void)
{
    //greet user
    string name = get_string("What is your name?\n");
    printf("hello, %s\n", name);
}