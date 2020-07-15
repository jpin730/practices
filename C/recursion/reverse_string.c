#include <stdio.h>
#include <string.h>

int reverseString(char dest[], char src[], int srcStrLength) {
  int processedChars = 1;
  char firstChar = src[0];
  if (firstChar == '\0') {
    return 0;
  }
  if (strlen(src) == srcStrLength) {
    dest[strlen(src)] = '\0';
  }
  dest[strlen(src)-1] = firstChar;
  reverseString(dest, src + 1, srcStrLength);
  return 0;
}

int main(int argc, char const *argv[]) {
  char string[] = "987654321";
  // char string[] = "This is string.h library function";
  char reverse[sizeof(string)];
  reverseString(reverse, string, strlen(string));
  printf("Original string:\n%s\nInverse string:\n%s\n", string, reverse);
  return 0;
}