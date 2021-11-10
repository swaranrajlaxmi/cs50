# include <stdio.h>
# include <cs50.h>
# include <math.h>

int main(void)
{
    long Number;
    // get user credit card number
    do
    {
        Number = get_long("Number: ");
    }
    while (Number < 1 || Number > 9999999999999999);
    // Apply luhn's algorithm for checksum
    long dividend = Number;
    int count = 0;
    int modulus;
    int sum;
    // check validity of number and credit length simultaneuosly. 
    while (dividend > 0)
    {
        modulus = dividend % 10;
        count++;
        // if counter is even then remaider will multiply by 2 and check further conditions
        if (count % 2 == 0)
        {
            if (modulus * 2 > 9)
            {
                sum = sum + ((modulus * 2) - 9);
            }
            else
            {
                sum = sum + (modulus * 2);
            }
        }
        //else simply add the remainder
        else
        {
            sum = sum + modulus;
        }
        
        dividend = dividend / 10;
            
    }
    //check for starting digits
    long starting_digit = Number;
    while (starting_digit > 99 || starting_digit < 9)
    {
        starting_digit = starting_digit / 10;
    }
    // if not satisfying luhn's algorithm then card number is invalid
    if (sum % 10 != 0)
    {
        printf("INVALID\n");
    }
    // else check below conditions and print accordingly.
    else
    {
        
        if (count == 16 && (starting_digit >= 51 && starting_digit <= 55))
        {
            printf("MASTERCARD\n");
        }
        else if (count == 15 && (starting_digit == 34 || starting_digit == 37))
        {
            printf("AMEX\n");
        }
        else if ((count == 13 || count == 16) && starting_digit >= 40 && starting_digit <= 49)
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    
    
}