#include <stdio.h>
#include <inttypes.h>

int main(void) {
	int64_t B, C;
	int64_t s1, e1, s2, e2;
	if (scanf("%" SCNd64 "%" SCNd64, &B, &C) != 2) return 1;
	s1 = -B-(C-1)/2;
	e1 = -B+(C-1)/2;
	s2 = B-C/2;
	e2 = B+(C-2)/2;
#if 0
	printf("%" PRId64 " %" PRId64 " %" PRId64 " %" PRId64 "\n", s1, e1, s2, e2);
#endif
	if (s1 > s2) {
		int64_t t;
		t = s1; s1 = s2; s2 = t;
		t = e1; e1 = e2; e2 = t;
	}
	if (e1 < s2) {
		printf("%" PRId64 "\n", (e1 - s1 + 1) + (e2 - s2 + 1));
	} else {
		printf("%" PRId64 "\n", ((e2 > e1 ? e2 : e1) - s1 + 1));
	}
	return 0;
}

/*

往復するのは効率が悪い
×-1, -1 * n           -B-(C-1)/2 ～ -B
×-1, -1 * n, ×-1     B ～ B+(C-2)/2
-1 * n                 B-C/2 ～ B
-1 * n, × -1          -B ～ -B+(C-1)/2

-B-(C-1)/2 ～ -B+(C-1)/2
B-C/2 ～ B+(C-2)/2

*/
