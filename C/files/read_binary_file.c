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
		printf("Enter input file name.\n");
		return -1;
	}

	if ( !( fp = fopen(argv[1], "r") ) ) {
		printf("File %s cannot be opened.\n", argv[1]);
		return -2;
	}

	struct person p;

	while ( fread(&p, sizeof(struct person), 1, fp) ) {
		printf("%s is %d years old.\n", p.name, p.age);
	}

	fclose(fp);

	return 0;
}
