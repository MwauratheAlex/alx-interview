#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void prime_sieve(int n);

int main() {
  // For 10mirrion
  // python time: It took 3.387782008998329
  // Time elapsed: 1.201008 seconds
  clock_t start_time = clock();
  prime_sieve(100);
  clock_t end_time = clock();

  double elapsed_time = (double)(end_time - start_time) / CLOCKS_PER_SEC;
  printf("Time elapsed: %f seconds\n", elapsed_time);
  return 0;
}

void prime_sieve(int n) {
  char *p = malloc(sizeof(char) * (n + 1));
  int i;
  for (i = 0; i <= n; i++) {
    p[i] = 1;
  }

  int prime = 2;

  while ((prime * prime) < (n + 1)) {
    if (p[prime] == 1) {
      int j;
      for (j = prime * prime; j < n + 1; j += prime) {
        p[j] = 0;
      }
    }
    prime += 1;
  }

  for (i = 2; i <= n; i++) {
    if (p[i] == 1) {
      printf("Prime: %d\n", i);
    }
  }

  free(p);
}
