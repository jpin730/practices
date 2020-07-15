#include <stdio.h>
#include <stdlib.h>

long result;

long factorial(int n){
  if (n == 0)
    return 1;
  else
    return n*factorial(n-1);
}

int main(int argc, char const *argv[]) {
  int n;
  if (argc > 1) {
    n = atoi(argv[1]);
    if (n > 0) {
      result = factorial(n);
      printf("%d! = %ld\n", n, result);
    }
    else
      printf("Number is not positive.\n");
  }
  else
    printf("Enter the number as argument.\n");
  return 0;
}