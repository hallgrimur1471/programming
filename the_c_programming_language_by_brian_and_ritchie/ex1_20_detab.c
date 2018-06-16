/* Write a program detab that replaces tabs in the input with the proper number
 * of blanks to space to the next tab stop. Assume a fixed set of tab stops,
 * say every n columns. Should n be a variable or a symbolic parameter? */

/* Answer:
 * If n is an external variable then other parts of the program can change
 * it's value, this might be desirable. */

#include <stdio.h>

int n;
void detab(int n);

main()
{
  n = 7;
  detab(n);
}

void detab(int n)
{
  char c;

  while ((c=getchar()) != EOF) {
    if (c == '\t') {
      for (int i=0; i<n; i++) {
        putchar(' ');
      }
    }
    else
      putchar(c);
  }
}
