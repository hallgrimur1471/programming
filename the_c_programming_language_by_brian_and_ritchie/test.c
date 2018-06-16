#include <stdio.h>

main()
{
  char a[6];
  a[0] = 'h';
  a[1] = 'e';
  a[2] = 'l';
  a[3] = 'l';
  a[4] = 'o';
  a[5] = '\n';
  a[6] = '\0';
  printf("%s", a);
  printf("%d", a[6]);

  printf("b:\n");
  char b[] = "hello\n";
  printf("%s", b);
  printf("%d\n", b[5]);
  printf("%d", b[6]);
}
