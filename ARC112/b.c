#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
int main(){
  long long int B,C,ans,A;
  scanf("%lld %lld",&B,&C);
  if(labs(B)*2>=C) ans=2*C-1;
  else{
    if(B>0){
      A=B+(C-1)/2;
      if(C%2==0) ans=2*A+1;
      else ans=2*A;
    }
    else{
       A=-B+C/2;
      if(C%2==0) ans=2*A;
      else ans=2*A+1;
    }
  }
  if(C==1 && B!=0) ans=2;
  printf("%lld",ans);
  return 0;
}