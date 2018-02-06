#include <pthread.h>

int a = 1;

void *brute(void *vargp) {
    while(1) {
        a = 1; a = 2; a = 3;
    }
}

int main() {
    pthread_t tid;
    pthread_create(&tid, NULL, brute, NULL);
    while(1) {
        if (a==1 && a==2 && a==3) {
            printf("pigs can fly\n");
            return;
        } else {
            printf("logical ...\n");
        }
    }
}
