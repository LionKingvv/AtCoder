#include <stdio.h>

int main(void) {
  int a, b, c, ans;
  scanf("%d %d %d", &a, &b, &c);
  
  ans = 21 - a - b - c;
  printf("%d\n", ans);
  return 0;
}