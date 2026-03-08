#include <stdio.h>
void setZeroes(int** matrix, int matrixSize, int* matrixColSize) {
    int zeroes_first_row = 0;
    int zeroes_first_col = 0;
    for(int i = 0; i < matrixSize ;i++){
        if(matrix[i][0] == 0){
            zeroes_first_col = 1;
            break;    
        }
    }
    for(int j = 0 ;j  < matrixColSize[0] ; j++){
        if(matrix[0][j] == 0){
            zeroes_first_row =1;
            break;
        }
    }


    // use first row and first col as markers
    for(int i = 1;i < matrixSize;i++){
        for(int j = 1 ;j < matrixColSize[i] ;j++){
            if(matrix[i][j] == 0){
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }

    for(int i = 1 ; i < matrixSize;i++){
        for(int j = 1 ;j  < matrixColSize[i] ;j++){
            if(matrix[i][0] ==0 || matrix[0][j] == 0)
            {
                matrix[i][j] =0;
            }
        }
    }
    if(zeroes_first_col){
        for(int i = 0 ; i < matrixSize;i++)
            matrix[i][0] = 0;
    }
    if(zeroes_first_row){
        for(int j = 0 ;j  < matrixColSize[0];j++){
            matrix[0][j] = 0;
        }
    }
    
}