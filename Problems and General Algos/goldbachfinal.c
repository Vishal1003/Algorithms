/* Goldbach's Conjecture -- says that any even  integer greater than 2 is the sum of two prime numbers (like 4 = 2 + 2;  8 = 3 + 5; 22 = 3 + 19 = 5 + 17 etc.).
 */
#include<stdio.h>
#include<stdlib.h>
void sieve(int *num,int n) // sieve method to find primes
{
  	int i,k,j,step;
	for(i=2;i<n;i++)
	{
		if(num[i]!=0)
		{
		
			k=num[i]*2;
			step=num[i];
			for(j=k;j<=n;j=j+step)
				num[j]=0;
		}		
	}	
}
int main() //main program
{
		long int n;
		scanf("%ld",&n);
		long int i;
		int *num=(int *)malloc(n*sizeof(long int));
		if(n%2==0)
		{for(i=0;i<n;i++)
			num[i]=i;
		sieve(num,n);
		for( i=4;i<=n/2;i++)
		{	
			if(num[i]+num[n-i]==n)
			{
				printf("%ld + %ld = %ld\n",i,n-i,n);
			}
		}
		}
		else
		printf("Enter an even number");
}
