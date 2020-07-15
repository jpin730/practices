#include <stdio.h>
#include <stdlib.h>

struct person {
	char name[100];
	unsigned int age;
};

int main (int argc, const char * argv[]) {
	FILE * fp; 
	char buffer[100];

	if (argc < 2) {
		printf("Enter output file name.\n");
		return -1;
	}

	if ( !( fp = fopen(argv[1], "w") ) ) {
		printf("File %s cannot be opened.\n", argv[1]);
		return -2;
	}

	struct person p;

	do {
		printf("Enter name: ");
		scanf("%99s", p.name);
		printf("Enter age: ");
		scanf("%d", &(p.age) );
		fwrite(&p, sizeof(struct person), 1, fp);
		printf("Continue? (y/n): ");
		scanf("%1s", buffer);
	} while(buffer[0] != 'n');

	fclose(fp);

	return 0;
}
