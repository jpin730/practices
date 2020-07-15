#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
	int number;
	struct Node * next;
} NODE;

NODE * createNode(int number) {
	NODE * newNode;
	newNode = malloc(sizeof(NODE));
	newNode->next = NULL;
	newNode->number = number;

	return newNode;
}

int main(int argc, const char * argv[]) {
	NODE * start = NULL, * current, * next; 
	int listSize = 0, number;
	do {
		printf("List Size = %d. Enter next number (0 to exit): ", listSize);
		scanf("%d", &number);
		
		if (number) {
			if (!start) {
				start = createNode(number);
			}
			else {
				current = start;
				while (current->next){
					current = current->next;
				}
				current->next = createNode(number);
			}
			listSize++;
		}
	} while (number);

	printf("Linked list:\n");
	current = start;
	while(current) {
		printf("%d", current->number);
		printf(current->next ? ", " : "\n");
		current = current->next;
	}	

	current = start;
	while (current) {
		next = current->next;
		free(current);
		current = next;
	}
	return 0;
}
