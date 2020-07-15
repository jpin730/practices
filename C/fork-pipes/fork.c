#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main() {
	int shared = 1;
	int pid = fork();
	
	if (pid) {
		printf("parent pid=%d shared=%d\n", getpid(), shared);
		wait(NULL);
		printf("Fork ended shared=%d.\n", shared);
	} else {
		shared = 0;
	       	printf("child pid=%d shared=%d\n", getpid(), shared);
		sleep(2);
	}
	
	return 0;
}
