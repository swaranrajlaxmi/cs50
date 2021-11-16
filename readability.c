# include <stdio.h>
# include <cs50.h>
# include <string.h>
# include <ctype.h>
# include <math.h>

int letters, sentences, x;
//set initial grade level
int index;

int main(void)
{
    //Get input text from the user
    string text = get_string("Text: ");
    
    //count for letters, words, and sentences in the text
    int n = strlen(text);
    int words = 1;
    
    for (int i = 0; i < n; i++)
    {
        if (isalnum(text[i]) || islower(text[i]) || isupper(text[i]))
        {
            letters++;
        }
        else if (isspace(text[i]))
        {
            words++;
        }
        else if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences++;
        }
        
    }
    printf("%i, %i, %i\n", letters, words, sentences);

    // calculate coleman liau index
    index = round(0.0588 * ((letters * 100) / (float) words) - 0.296 * ((sentences * 100) / (float)words) - 15.8);
    

    //grade level
    x = index;
    printf("%i\n", x);

    //TODO: print the grade level of the text
    if (x >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (x <= 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", x);
    }

   
}