/* Write a program to count blanks, tabs, and newlines. */

#include <stdio.h>

main()
{
  int c;
  int blanks, tabs, newlines;

  blanks = tabs = newlines = 0;
  while ((c = getchar()) != EOF) {
    if (c == ' ')
      ++blanks;
    else if (c == '\t')
      ++tabs;
    else if (c == '\n')
      ++newlines;
  }
  printf("%d %d %d\n", blanks, tabs, newlines);
}
