#include <stdio.h>
#include <stdlib.h>

int ec[114514];
int* es[114514];

void ae(int f, int t) {
	es[f] = realloc(es[f], sizeof(*es[f]) * (ec[f] + 1));
	if (es[f] == NULL) exit(2);
	es[f][ec[f]++] = t;
}

struct chousa_kekka {
	int is_same; /* 入る人(入った時から見たら後手)が、出る(ゲームを終える)か */
	int hairu_count; /* 入る人の得るコイン */
	int opp_count; /* 入る人じゃない方の得るコイン */
};

/*
xがyより先に来てほしい → 負
xがyより後に来てほしい → 正
*/
int cmp(const void* x, const void* y) {
	struct chousa_kekka a = *(const struct chousa_kekka*)x, b = *(const struct chousa_kekka*)y;
	int as = a.hairu_count - a.opp_count;
	int bs = b.hairu_count - b.opp_count;
	if (as >= 0 && bs >= 0) {
		if (!a.is_same && b.is_same) {
			return -1;
		} else if (a.is_same && !b.is_same) {
			return 1;
		} else {
			return as > bs ? -1 : as < bs;
		}
	} else if (as >= 0 && bs < 0) {
		return -1;
	} else if (as < 0 && bs >= 0) {
		return 1;
	} else {
		if (a.is_same && !b.is_same) {
			return -1;
		} else if (!a.is_same && b.is_same) {
			return 1;
		} else {
			return as > bs ? -1 : as < bs;
		}
	}
}

struct chousa_kekka chousa(int node) {
	struct chousa_kekka res;
	if (ec[node] == 0) {
		res.is_same = 1;
		res.hairu_count = 0;
		res.opp_count = 1;
	} else {
		struct chousa_kekka* ko = malloc(sizeof(*ko) * ec[node]);
		int i;
		if (ko == NULL) exit(2);
		for (i = 0; i < ec[node]; i++) {
			ko[i] = chousa(es[node][i]);
		}
		qsort(ko, ec[node], sizeof(*ko), cmp);
		res.is_same = 1;
		res.hairu_count = 0;
		res.opp_count = 1;
		for (i = 0; i < ec[node]; i++) {
			if (res.is_same) {
				res.hairu_count += ko[i].hairu_count;
				res.opp_count += ko[i].opp_count;
			} else {
				res.hairu_count += ko[i].opp_count;
				res.opp_count += ko[i].hairu_count;
			}
			if (ko[i].is_same) res.is_same = !res.is_same;
		}
		free(ko);
	}
#if 0
	printf("node=%d is_same=%d, hairu=%d, opp=%d\n", node, res.is_same, res.hairu_count, res.opp_count);
#endif
	return res;
}

int main(void) {
	int n;
	int i;
	struct chousa_kekka res;
	if (scanf("%d", &n) != 1) return 1;
	for (i = 2; i <= n; i++) {
		int p;
		if (scanf("%d", &p) != 1) return 1;
		ae(p, i);
	}
	res = chousa(1);
	printf("%d\n", res.opp_count);
	return 0;
}

/*

is_sameが0 → もう1回同じ人
is_sameが1 → 交代

is_sameが1の子が奇数 → このノードはis_sameが0
is_sameが1の子が偶数 → このノードはis_sameが1

最初は入る人が選べる

node 6

is_same hairu opp
0       0     2
1       0     1
1       0     1

(予想)
交代せずに得(or 0) > 交代して得(or 0) > 交代して損 > 交代せずに損

*/
