#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (int argc, const char * argv[]) {
	FILE * fp;
	char buffer[100];
	if( !( fp = fopen( argv[1], "w" ) ) ) {
		printf("File cannot be opened\n");
		return -1;
	}
	do {
		printf("Enter a word: ");
		scanf("%99s", buffer);
		fputs(buffer, fp);
		fputs("\n",fp);
		printf("Do you want to enter another word? (y/n): ");
		scanf("%1s", buffer);
	} while(buffer[0] != 'n');

	fclose(fp);

	return 0;
}
