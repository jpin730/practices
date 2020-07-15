#include <stdio.h>

// PRINT ARRAY

void printArray(int array[], int arraySize) {
  for (int i = 0; i < arraySize; i++) {
    printf("%d", array[i]);
    if (i != arraySize-1)
      printf(", ");
    else
      printf(".\n");
  }
}

// COPY ARRAY

void copyArray(int destArray[], int srcArray[], int arraySize) {
  for(int i = 0; i < arraySize; i++) {
    destArray[i]=srcArray[i];
  }
}

// SWAP PAIR OF ELEMENT FROM ARRAY

void swapPair(int* a, int* b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

// BUBBLE SORT

int bubbleSort(int array[], int arraySize) {
  int swapPair2;
  if (arraySize < 2) {
    return 0;
  }
  for (int swapPair1 = 0; swapPair1 < arraySize - 1; swapPair1++) {
    swapPair2 = swapPair1 + 1;
    if (array[swapPair1] > array[swapPair2]) {
      swapPair(&array[swapPair1], &array[swapPair2]);
    }
  }
  bubbleSort(array, arraySize-1);
  return 0;
}

//  INSERTION SORT

void insertionSort(int array[], int arraySize) {
  int toBeInsertedValue, comparedIndex, comparedValue;
  for (int toBeInsertedIndex = 1; toBeInsertedIndex < arraySize; toBeInsertedIndex++) { 
    toBeInsertedValue = array[toBeInsertedIndex];
    comparedIndex = toBeInsertedIndex - 1;
    while (comparedIndex >= 0 && array[comparedIndex] > toBeInsertedValue) {
      array[comparedIndex + 1] = array[comparedIndex];
      comparedIndex--;
    }
    array[comparedIndex + 1] = toBeInsertedValue; 
  }
}

// MERGE SORT

void sortAndMergeSubArrays(int subArray1[], int subArray1Size, int subArray2[], int subArray2Size) {
  int tempSubArray1[subArray1Size + 1]; 
  int tempSubArray2[subArray2Size + 1];
  copyArray(tempSubArray1, subArray1, subArray1Size);
  copyArray(tempSubArray2, subArray2, subArray2Size);
  tempSubArray1[subArray1Size] = __INT_MAX__;
  tempSubArray2[subArray2Size] = __INT_MAX__;
  int *mergedArrayPtr = subArray1;
  int mergedArraySize = subArray1Size + subArray2Size;
  int subArray1Index = 0;
  int subArray2Index = 0;
  for (int i = 0; i < mergedArraySize; i++) {
    if ( tempSubArray1[subArray1Index] <= tempSubArray2[subArray2Index] ) {
      *(mergedArrayPtr) = tempSubArray1[subArray1Index++];
    }
    else {
      *(mergedArrayPtr) = tempSubArray2[subArray2Index++]; 
    }
    mergedArrayPtr++;
  }
}

int mergeSort(int array[], int arraySize) {
  if (arraySize > 1) {
    int subArray1Size = arraySize/2, subArray2Size;
    if (arraySize % 2 == 0) {
      subArray2Size = arraySize/2;
    }
    else {
      subArray2Size = arraySize/2 + 1;
    }
    int *subArray1 = array;
    int *subArray2 = array + subArray1Size;    
    mergeSort(subArray1, subArray1Size);
    mergeSort(subArray2, subArray2Size);
    sortAndMergeSubArrays(subArray1, subArray1Size, subArray2, subArray2Size);
  }
  return 0;
}

// QUICK SORT

int quickSort(int array[], int arraySize) {
  if (arraySize > 1) {
    int partitionIndex = 0;
    for (int i = 0; i < arraySize; i++) {
      if (array[i] <= array[arraySize-1]) {
        swapPair(&array[i], &array[partitionIndex]);
        partitionIndex++;
      }
    }
    partitionIndex--;
    int subArray1Size = partitionIndex;
    int subArray2Size = arraySize - partitionIndex - 1;
    if (subArray1Size > 1) {
      int *subArray1 = array;
      quickSort(subArray1, subArray1Size);
    }
    if (subArray2Size > 1) {
      int *subArray2 = array + partitionIndex + 1;
      quickSort(subArray2, subArray2Size);
    }
  }
  return 0;
}


// CLOCK CICLES

#include <time.h>
clock_t start_t, end_t, total_t;

void tic() {
  start_t = clock();
}

void toc() {
  end_t = clock();
  total_t = end_t - start_t;
  printf("CPU Cicles = %ld\n", total_t);
}

// MAIN

int main(int argc, char const *argv[]) {
  int array[] = {100, 1992, 0, -1, 60, 70, 14, 15, -100, 10};
  int arraySize = sizeof(array)/sizeof(int);
  int tempArray[arraySize];
  copyArray(tempArray, array, arraySize);
  printf("Bubble Sort:\n");
  printArray(array, arraySize);
  tic();
  bubbleSort(array, arraySize);
  toc();
  printArray(array, arraySize);
  copyArray(array, tempArray, arraySize);
  printf("\nInsertion Sort:\n");
  printArray(array, arraySize);
  tic();
  insertionSort(array, arraySize);
  toc();
  printArray(array, arraySize);
  copyArray(array, tempArray, arraySize);
  printf("\nMerge Sort:\n");
  printArray(array, arraySize);
  tic();
  mergeSort(array, arraySize);
  toc();
  printArray(array, arraySize);
  copyArray(array, tempArray, arraySize);
  printf("\nQuick Sort:\n");
  printArray(array, arraySize);
  tic();
  quickSort(array, arraySize);
  toc();
  printArray(array, arraySize);
  return 0;
}