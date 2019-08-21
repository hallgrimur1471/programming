#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <limits.h>

// ./print_bytes 97 98 99 10
// abc
int main(int argc, char* argv[]){
  char* s;
  int n;
  char c;

  argv++; // skip program name

  while (*argv != '\0') {
    s = *argv;
    n = atoi(s);
    c = n;

    printf("%c", c);

    argv++;
  }

  return 0;
}
