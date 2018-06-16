/* Write a program to print a histogram of the lengths of word in
 * its input. It is easy to draw the histogram with the bars horizontal; a vertical
 * orientation is more challenging. */

#include <stdio.h> 

#define IN 1 /* inside a word */
#define OUT 0 /* outside a word */

#define MAX_LENGTH 20 /* histogram will show words of length 1 to MAX_LENGTH */

main()
{
  int c, cl, state;
  int nchars[MAX_LENGTH];

  c = cl = 0;
  state = OUT;
  for (int i=0; i < MAX_LENGTH; i++) {
    nchars[i] = 0;
  }

  while ((c = getchar()) != EOF) {
    if (c == ' ' || c == '\n' || c == '\t') {
      state = OUT;
      if (cl <= MAX_LENGTH)
        ++nchars[cl];
      cl = 0;
    }
    else {
      state = IN;
      ++cl;
    }
  }
  if (cl <= MAX_LENGTH)
    ++nchars[cl];

  for (int i=1; i < MAX_LENGTH; i++) {
    printf("%2d: ", i);
    for (int j=0; j < nchars[i]; j++) {
      printf("|");
    }
    printf("\n");
  }
}
