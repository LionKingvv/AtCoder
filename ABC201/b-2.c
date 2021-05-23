#include<stdio.h>
#include<string.h>
main()
{

int a[1000],max,i,j,n,t;
char b[1000][20],k[20],c;
scanf("%d",&n);
for(i=0;i<n;i++)
{   j=0;
    while(scanf("%c",&c)&&c!=' ')
	b[i][j++]=c;
	b[i][j]=0;
	scanf("%d",&a[i]);
}
for(i=0;i<n-1;i++)
for(j=i+1;j<n;j++)
{if(a[i]>a[j])
{t=a[i];a[i]=a[j];a[j]=t;strcpy(k,b[i]);strcpy(b[i],b[j]);strcpy(b[j],k);}
}
puts(b[n-2]);
}