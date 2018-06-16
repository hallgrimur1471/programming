/* Write a program that prints its input one word per line. */

#include <stdio.h>

#define IN 1
#define OUT 0

main()
{
  int c, state;

  state = OUT;
  while ((c = getchar()) != EOF) {
    if (c != ' ' && c != '\n' && c != '\t') {
      state = IN;
    }
    else if (state == IN) {
      state = OUT;
      putchar('\n');
    }

    if (c != '\n')
      putchar(c);
  }
}
