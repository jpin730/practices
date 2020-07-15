#include <stdio.h>
#define SIZE 5

int queue[SIZE], front = -1, rear = -1;

void enQueue(int value) {
  if (rear == SIZE-1)
    printf("Queue is Full\n");
  else {
    if (front = -1)
      front = 0;
    rear++;
    queue[rear] = value;
    printf("Item %d added.\n", queue[rear]);
  }
}

void deQueue() {
  if (front == -1)
    printf("Queue is Empty\n");
  else {
    printf("Item deleted: %d\n", queue[front]);
    front++;
    if (front > rear)
      front = rear = -1;
  }
}

int main(int argc, char const *argv[]) {
  enQueue(1);
  enQueue(2);
  enQueue(3);
  enQueue(4);
  enQueue(5);
  enQueue(6);
  deQueue();
  deQueue();
  deQueue();
  deQueue();
  deQueue();
  enQueue(10);
  return 0;
}
