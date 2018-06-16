/* Write a program to print all input lines that are
 * longer than 80 characters */

#include <stdio.h>
#define MAXLINE 82 /* maximum input line size */

int getline(char line[], int maxline);
void copy(char to[], char from[]);

/* print longest input line */
main()
{
  int len; /* current line length */
  int tmp_len;
  int max; /* maximum length seen so far */
  char line[MAXLINE]; /* current input line */
  char longest[MAXLINE]; /* longest line saved here */
  char tmp_line[MAXLINE]; /* pass this to getline when line and longest should not be overwritten */

  max = 0;
  while ((len = getline(line, MAXLINE)) > 0) {
    if (len > MAXLINE-2) {
      printf("%s", line);
      while (len==MAXLINE-1 && line[MAXLINE-1]!='\n') {
        len = getline(line, MAXLINE);
        printf("%s", line);
      }
    }
  }
  return 0;
}

/* getline: read a line into s, return length */
int getline(char s[], int lim)
{
  int c, i;

  for (i=0; i<lim-1 && (c=getchar())!=EOF && c!='\n'; ++i)
    s[i] = c;
  if (c == '\n') {
    s[i] = c;
    ++i;
  }
  s[i] = '\0';
  return i;
}

/* copy: copy 'from' into 'to'; assume to is big enough */
void copy (char to[], char from[])
{
  int i;

  i = 0;
  while ((to[i] = from[i]) != '\0')
    ++i;
}
