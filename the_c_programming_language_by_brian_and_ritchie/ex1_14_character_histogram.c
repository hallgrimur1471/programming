/* Write a program to print a histogram of the frequencies of different
 * characters in its input. */

#include <stdio.h> 

#define IN 1 /* inside a word */
#define OUT 0 /* outside a word */

/* histogram will be of characters with
 * int values from ASCII_START to ASCII_END */
#define ASCII_START (' '+0)
#define ASCII_END ('~'+0)

main()
{
  int c;
  int L = ASCII_END-ASCII_START;
  int nchars[L];

  for (int i=0; i < L; i++) {
    nchars[i] = 0;
  }

  while ((c = getchar()) != EOF) {
    if (ASCII_START <= c && c < ASCII_END)
      ++nchars[c-ASCII_START];
  }
  for (int i=0; i < L; i++) {
    printf("%c: ", i+ASCII_START);
    for (int j=0; j < nchars[i]; j++) {
      printf("|");
    }
    printf("\n");
  }
}
