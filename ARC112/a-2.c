#include <stdio.h>
#include <inttypes.h>

uint64_t wa(uint64_t a, uint64_t d, uint64_t n) {
	return n * (2 * a + (n - 1) * d) / 2;
}

int main(void) {
	int T;
	int i;
	if (scanf("%d", &T) != 1) return 1;
	for (i = 0; i < T; i++) {
		int L, R;
		if (scanf("%d%d", &L, &R) != 2) return 1;
		printf("%" PRIu64 "\n", (R-L)-L+1 > 0 ? wa(1, 1, (R-L)-L+1) : 0);
	}
	return 0;
}

/*

C=L     (A, B) = (L + C, L), (L + C + 1, L + 1), ... , (R, R - C)
C=L+1
...
C=R-L   (A, B) = (R, L)

初項1 公差1 項数(R-L)-L+1

等差数列の和 https://www.kwansei.ac.jp/hs/z90010/sugakua/suuretu/tousasum/tousasum.htm

*/
