#include <stdio.h>
#include <stdlib.h>

int** matrixReshape(int** mat, int matSize, int* matColSize, int r, int c, int* returnSize, int** returnColumnSizes) {
    int originalSize = matSize * matColSize[0];
    int newSize = r * c;

    // If reshape is invalid OR already same shape, return original
    if (newSize != originalSize || (matSize == r && matColSize[0] == c)) {
        *returnSize = matSize;
        *returnColumnSizes = matColSize;
        return mat;
    }

    // Allocate new matrix
    int** newMat = (int**)malloc(sizeof(int*) * r);
    *returnColumnSizes = (int*)malloc(sizeof(int) * r); 
    *returnSize = r;

    for (int i = 0; i < r; i++) {
        newMat[i] = (int*)malloc(sizeof(int) * c);
        (*returnColumnSizes)[i] = c;  
    }

    int prevC = matColSize[0];

    // Flatten and refill
    for (int i = 0; i < newSize; i++) {
        newMat[i / c][i % c] = mat[i / prevC][i % prevC];
    }

    return newMat;
}