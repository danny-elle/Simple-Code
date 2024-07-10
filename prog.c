#include<stdio.h>
#include<string.h>

int strlength(char arr[]);
int strcomp(char *s, char *t);

int main(int argc, char *argv[])
{

	puts("Here is my sentence.\n");

	char arr[]="any string you want";
	char str[]="any string you wont";

	printf("length of arr: %d\n",strlength(arr));
	
	printf("string compare: %d\n", strcmp(arr, str));
	printf("string compare: %d\n", strcomp(arr, str));
   	return 0;
}

int strlength(char arr[])
{
	char *s = arr;
	int count;
	count = 0;
	for(; *s != '\0'; s++ )
	{
		count++;
	}
	return count;
}

int strcomp(char *s, char *t)
{
	
	while ( *s && *t )
	{
		if (*s == *t )
		{
			s++;
			t++;
		}else{
			break;
		}
	}	
	return *s-*t;
	
	
}
