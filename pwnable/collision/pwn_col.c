#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>

void elegant() {
  //unsigned long desired_hashcode = 0x21DD09EC;
  //printf("Desired hashcode %x\n", desired_hashcode);

  //unsigned long value_of_4_bytes = desired_hashcode / 5;
  //printf("Each 4 bytes should have value of %x\n", value_of_4_bytes);
  
  // ...
  return;
}


char* generate_random_valid_password(char* password) {
  for (int i = 0; i < 20; i++) {
    password[i] = rand() % 256 - 128;
  }
  password[20] = '\0';
  return password;
}

unsigned long password_hashcode(const char* p){
	int* ip = (int*)p;
	int i;
	int res=0;
	for(i=0; i<5; i++){
		res += ip[i];
	}
	return res;
}

void brute_force() {
  unsigned long desired_hascode = 0x21DD09EC;
  unsigned long result;
  char password[21];

  // shuffle rand()
  srand(time(NULL));

  generate_random_valid_password(password);
  result = password_hashcode(password);
  while (result != desired_hascode) {
    generate_random_valid_password(password);
    result = password_hashcode(password);
  }

  for (int i = 0; i < 20; i++) {
    printf("%d ", password[i]);
  }
  printf("\n");
}

int main(int argc, char* argv[]) {
  //elegant();
  brute_force();
  return 0;
}
