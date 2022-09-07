//Francisco Hernandez Jr.
//Jonathan Leal
//Samuel Lee
//Edwin Lozano
#include <stdio.h>
#include <stdlib.h>
int avg(int sum, int count);
int main() {
	int sum = 0;
	int count = 0;
	FILE* infile;
	infile = fopen("input9.txt", "r");
	int number;
  if(infile == NULL){
    
    printf("The average is: 0");
    return 0;
  }
  else{

	while (fscanf(infile,"%d", &number) !=EOF)
	{
    count++;
		printf("%d: %d \n", count, number);
    
    sum = sum + number;
	}
  if(count == 0)
  {
    printf("The average is: 0");
    return 0;
  }
  int avgr = avg(sum, count);
	fclose(infile);
	printf("\n\nThe Average is: %d \n", avgr);
  }


return (0);

}