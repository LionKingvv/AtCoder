// #include <stdio.h>
// #include <stdlib.h>

// struct mountain {
//   char s[100000];
//   int t;
// };

// void qqsort(struct mountain abc[], int left, int right)
// {
// struct mountain num; //変更
// int big;
// int small;
// int f;
// struct mountain temp; //変更
// if (left < right) {
// num = abc[left]; //変更
// big = left + 1;
// small = right;
// f = 0;
// while (f == 0) {
// while ((abc[big].t <= num.t) && (big < right)) // num.id に変更
// big++;
// while ((abc[small].t >= num.t) && (small > left))// num.id に変更
// small--;
// if (big < small) {
// // ①
// temp = abc[big];//変更
// abc[big] = abc[small];//変更
// abc[small] = temp;//変更
// } else
// f = -1;
// }
// abc[left] = abc[small];
// abc[small] = num;//変更
// qqsort(abc, left, small - 1);
// qqsort(abc, small + 1, right);
// }
// }

// int main(void) {
//   int n;
//   scanf("%d", &n);
//   struct mountain mt[n];
 
//   for(long long i = 0; i < n; i++) {
//     scanf("%s %d", mt[i].s, &mt[i].t);
//   }

//   // for(int i = 0; i < n; i++) printf("%s\n", s[i]);


//   qqsort(mt, 0, n);

//   // for(int i = 0; i < n; i++) printf("%s\n", s[i]);

//   printf("%s\n", mt[1].s);
//   return 0;
// }


#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

typedef struct mont{
    char nome_mont[20];
    int alt;
} mont;

mont *montes;

int func(const void *a, const void *b){
    const mont *x = a, *y = b;
    if(x->alt < y->alt)
        return -1;
    if(x->alt > y->alt)
        return 1;
    return 0;
}

int main() {
    int n;
    scanf("%d", &n);
    montes = malloc(n * sizeof(mont));
    for(int i = 0; i < n; i++){
        scanf("%s %d", montes[i].nome_mont, &montes[i].alt);
    }
    qsort(montes, n, sizeof(montes[0]), func);
    printf("%s", montes[n-2].nome_mont);
    free(montes);
    return 0;
}