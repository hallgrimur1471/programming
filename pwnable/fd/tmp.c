#include "unistd.h"
char buf[32];
int main(int argc, char* argv[], char* envp[]){
  int fd = 0;
	int len = read(fd, buf, 32);
	return 0;
}
