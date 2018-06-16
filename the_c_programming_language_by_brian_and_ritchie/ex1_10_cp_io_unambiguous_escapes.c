/* Write a program to copy its input to its output, replacing each
 * tab by \t, each backspace by \b, and each backslash by \\. This makes tabs
 * and backspaces visible in an unambiguous way. */

/* Extra: I also replace new-lines by \n */

#include <stdio.h>

main()
{
  int c;

  while ((c = getchar()) != EOF) {
    if (c == '\t') {
      putchar('\\');
      putchar('t');
    }
    else if (c == '\b') {
      putchar('\\');
      putchar('b');
    }
    else if (c == '\n') {
      putchar('\\');
      putchar('n');
    }
    else if (c == '\\') {
      putchar('\\');
      putchar('\\');
    }
    else {
      putchar(c);
    }
  }
}
