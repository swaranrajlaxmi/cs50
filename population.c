# include <stdio.h>
# include <cs50.h>
int main(void)
{
   int start_size;
   int end_size;
   int n=0;
  do
  {
      start_size = get_int("Start size: ");
  }
  while (start_size < 9);
  
  do
  {
      end_size = get_int("End size: ");
  }
  while (end_size < start_size);
  
 
      
  
  
  while (start_size < end_size)
  {
      start_size = start_size + start_size/3 - start_size/4;
      n++;
  }
  
  printf("Years: %d \n", n);
}