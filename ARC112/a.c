#include <stdio.h>

int main(void) {
  long long L, R, k;
  scanf("%*d");
 
  while (~scanf("%lld %lld", &L, &R)) {
    if (L == R) {
      if (L == 0) {
        printf("1");
      } else {
        printf("0");
      }
    } else {
      k=R-L*2+1;
      if (k>0) {
        printf("%lld", k * (k+1) / 2);
      } else {
        printf("0");
      }
    }
    printf("\n"); 
  }

  return 0;
}
