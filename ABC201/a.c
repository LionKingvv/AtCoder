#include <stdio.h>
#include <stdlib.h>

int main(void) {
  long long a[3];
  scanf("%lld %lld %lld", &a[0], &a[1], &a[2]);
 
  for(int i = 0; i < 3; i++) {
    for(int j = 0; j < 3; j++) {
      if(i == j) continue;
      if((a[i] - a[j]) == (a[j] - a[abs(3-i-j)])) {
        printf("Yes\n");
        return 0;
      }
    }
  }

  printf("No\n");
  return 0;
}