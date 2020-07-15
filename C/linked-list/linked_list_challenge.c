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
	NODE * start = NULL, * current, * next, * before;
	int listSize = 0, number, node;
	do {
		printf("List Node %d. Enter next number (0 to exit): ", listSize);
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
	
	do {
		printf("Linked list:\n");
		current = start;
		while(current) {
			printf("%d", current->number);
			printf(current->next ? ", " : "\n");
			current = current->next;
		}	

		do {
		printf("Which node do you want to remove? 1-%d (0 to exit): ", listSize);
		scanf("%d", &node);
		} while(node > listSize);

		if (node == 1) {
			before = start;
			start = start->next;
			free(before);
			listSize--;
		} else if (node > 1) { 
			current = start;
			for (int i = 1; i < node; i++) {
				before = current;
				current = current->next;
			}
			before->next = current->next;
			free(current);
			listSize--;
		}
	} while (node > 0);


	current = start;
	while (current) {
		next = current->next;
		free(current);
		current = next;
	}
	return 0;
}
