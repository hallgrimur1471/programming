/* Write a program entab that replaces strings of blanks by the minimum number
 * of tabs and blanks to achieve the same spacing. Use the same tab stops
 * as for detab. When either a tab or a single blank would suffice
 * to reach a tab stop, which should be given preference? */

#include <stdio.h>

int n;
void entab(int n);

main()
{
  n = 7;
  entab(n);
}

void entab(int n)
{
  int spaces;
  char c;

  spaces = 0;
  while ((c = getchar()) != EOF) {
    if (c==' ') {
      ++spaces;
    }
    else {
      while (spaces >= n) {
        putchar('\t');
        spaces -= n;
      }
      while (spaces > 0) {
        putchar(' ');
        --spaces;
      }
      putchar(c);
    }
  }
}
