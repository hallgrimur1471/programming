#include <stdio.h>
#include "factorial.h"

int factorial(int n) {
  int f = 1;
  for (int i=1; i <= n; i++) {
    f = i*f;
  }
  return f;
}
