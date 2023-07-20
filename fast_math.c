#include <stdio.h>

int multiply_matrix(int a[], int b[], int rows, int cols){
    int i;
    int j;
    int result[rows][cols];
    for(i=0;i<=rows;i++){
        for(j=0;j<=cols;j++){
            result[i][j] = a[i][j] * b[i][j] ;
        }
    }

    return result; 
}

void hello_world(){
    printf("hello world\n")
}