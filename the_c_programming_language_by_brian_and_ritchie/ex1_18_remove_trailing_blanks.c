/* Write a program to remove trailing blanks and tabs from each line of input,
 * and to delete entirely blank lines. */

#include <stdio.h>

#define MAXLINE 40
#define MAXBLANKS 10
#define IN 1
#define OUT 0

main()
{
  int state, i, bi;
  char c;
  char buffer[MAXBLANKS];

  i = bi = 0;
  state = OUT;
  while ((c = getchar()) != EOF) {
    if (c!=' ' && c!='\t' && c!='\n') {
      state = IN;
      for (i=0; i<bi; i++) {
        putchar(buffer[i]);
      }
      bi = 0;
      putchar(c);
    }
    else {
      state = OUT;
      if (c == '\n')
        putchar(c);
      else {
        buffer[bi] = c;
        ++bi;
      }
    }
  }
}
