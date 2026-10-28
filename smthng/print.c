#include <stdio.h>

int main(void){
    int A[8] = {-7,12,13,16,23,90,122,0};
    int B[4] = {12, 14, 25,0};
    int C[12] = {0};

    extern void merge(int A[], int B[], int C[])

    int size = sizeof(C) / sizeof(C[0]);

    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
        printf(", ");
    }
}
