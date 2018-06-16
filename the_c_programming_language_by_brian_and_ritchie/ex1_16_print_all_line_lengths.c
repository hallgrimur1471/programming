/* Revise the main routine of the longest-line program so it will correctly print
 * the length of arbitrarily long input lines, and as much as possible of text */

#include <stdio.h>
#define MAXLINE 30 /* maximum input line size */

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
    if (len ==MAXLINE-1 && line[MAXLINE-1]!='\n') { /* the line might be longer */
      copy(tmp_line, line);
      tmp_len = len;
      while (tmp_len==MAXLINE-1 && tmp_line[MAXLINE-1]!='\n') {
        tmp_len = getline(tmp_line, MAXLINE);
        len += tmp_len;
      }
    }
    if (len > max) {
      max = len;
      copy(longest, line);
    }
    printf("%d\n", len);
  }
  if (max > 0) /* there was a line */
    printf("%s", longest);
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
