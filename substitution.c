# include <stdio.h>
# include <cs50.h>
# include <string.h>
# include <stdlib.h>
# include <ctype.h>

int main(int argc, string argv[])
{
    //TODO: check for single command line arguments and validate key
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    //TODO: check for length 26 characters
    if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters\n");
        return 1;
    }
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        //TODO: check for non-alpha characters
        if (! isalpha(argv[1][i]))
        {
            printf("Key must only contain alphabetic characters\n");
            return 1;
        }
        //TODO: check for repeated characters
        for (int l = i + 1; l < strlen(argv[1]); l++)
        {
            if (toupper(argv[1][l]) == toupper(argv[1][i]))
            {
                printf("Key must not contain repeated characters\n");
                return 1;
            }
        }
    }
    //TODO: Get plaintext:
    string text = get_string("plaintext:  ");
    //encipher
    printf("ciphertext: ");
    char *k = (argv[1]);
    for (int i = 0; i < strlen(text); i++)
    {
        if (isupper(text[i]))
        {
            int value = text[i] - 65;
            printf("%c", toupper(k[value]));
        }
        else if (islower(text[i]))
        {
            int value = text[i] - 97;
            printf("%c", tolower(k[value]));
        }
        else
        {
            printf("%c", text[i]);
        }
    }
    printf("\n");
}