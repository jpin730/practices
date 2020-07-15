#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef char NAME[100];
typedef char EMAIL[100];

typedef struct {
	NAME name;
	EMAIL email;
} CONTACT;

int main(int argc, const char * argv[]) {
	CONTACT * list = NULL;
	char buffer[100];
	int goOn, listSize = 0;

	do {
		printf("Enter the name of the new contact (0 to exit): ");
		scanf("%99s", buffer);

		if (strcmp("0", buffer)) {
			
			if (!list) {
				list = malloc(sizeof(CONTACT));
			} else {
				list = realloc(list, sizeof(CONTACT)*(listSize+1));
			}
			strcpy(list[listSize].name, buffer);
			
			printf("Enter the %s\'s e-mail: ", buffer);
			scanf("%99s", buffer);
			strcpy(list[listSize].email, buffer);

			goOn=1;
			listSize++;

		} else goOn = 0;
	} while(goOn);

	printf("\n Contact List:\n");	
	printf("Name\t\tEmail\n");
	for (int i = 0; i < listSize; i++) {
		printf("%s\t\t%s\n", list[i].name, list[i].email);
	}
	free(list);
	return 0;
}
