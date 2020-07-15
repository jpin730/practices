#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef char NAME[100];
typedef int AGE;

struct PERSON {
	NAME name;
	AGE age;
};

void fillPersonData (struct PERSON * person, const char * name, int age) {
 	if(strlen(name) < 100) {
 	       strcpy(person->name, name);
 	}
	person->age = age;
}

int main (int argc, const char * argv[]) {
	struct PERSON person;

	if (argc < 3) {
		printf("Introduce name and age, please.\n");
		return 1;
	}

	fillPersonData(&person, argv[1], atoi(argv[2]));

	printf("Name = %s, Age = %d\n", person.name, person.age);

	return 0;
}
