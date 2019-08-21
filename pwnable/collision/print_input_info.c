#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[]){
  printf("%zu %d+%d\n", strlen(argv[1]), argv[1][0], argv[1][1]);
  return 0;
}
