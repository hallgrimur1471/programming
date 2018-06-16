/* Write a function reverse(s) that reverses the character string s.
 * Use it to write a program that reverses it's input
 * line at a time. */

#include <stdio.h>

#define MAXLINE 1000

int getline(char line[], int maxline);
void reverse(char d[], char s[]);

main()
{
  int len;
  char line[MAXLINE];
  char reversed[MAXLINE];

  while ((len = getline(line, MAXLINE)) > 0 ) {
    reverse(reversed, line);
    printf("%s", reversed);
  }
}

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

void reverse(char d[], char s[])
{
  int i;
  int j;

  j = 0;
  for (i=0; s[i]!='\0'; i++)
    ++j;
  for (i=0; i < j; i++)
    d[i] = s[j-i-1]; 
  d[j] = '\0';
}
