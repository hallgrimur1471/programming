/* Write a program to copy its input to its output, replacing each
 * string of one or more blanks by a single blank. */

#include <stdio.h>

main()
{
  int c, lc;

  while ((c = getchar()) != EOF) {
    if (c!=' ' || lc!=' ')
      putchar(c);
    lc = c;
  }
}
