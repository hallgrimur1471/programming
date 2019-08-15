#include <stdio.h>
#include <unistd.h>
#include <limits.h>

int main(int argc, char* argv[]){
  char input_char = 128;
  char input_string[2];
  input_string[0] = input_char;
  input_string[1] = 0;

  execl("./print_input_info", "./print_input_info", input_string,(char*) NULL);
  return 0;

  // figured out that CHAR_MIN=-128 and CHAR_MAX=127 ...
}
