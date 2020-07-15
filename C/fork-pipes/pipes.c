#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <wait.h>

#define MSGSIZE 16

int main(int argc, const char * argv[]) {
	FILE * fp;
	int pid, p[2];
	
	if (pipe(p) < 0) {
		printf("Pipe were not created.\n");
		return -2;
	}

	if ( !( fp = fopen( argv[1], "r") ) ) {
		printf("File cannot be opened.\n");
		return -1;
	}

	if ( pid = fork() ) {
		char buffer[MSGSIZE];
		printf("parent: reading from file '%s'\n", argv[1]);
		while ( fgets(buffer, MSGSIZE, fp) ) {
			printf("I read '%s' pid=%d tell me the biggest char?\n", buffer, pid);
			write(p[1], buffer, MSGSIZE);
		}
		close(p[1]);
		printf("Waiting child\n");
		wait(NULL);
		fclose(fp);
	} else {
		close(p[1]);
		printf("children: waiting pipe message.\n");
		char buffer[MSGSIZE], max;
		while ( read(p[0], buffer, MSGSIZE) > 0 ) {
			printf("I read '%s' from pipe. ", buffer);
			max = buffer[0];
			for (int i = 0; i < MSGSIZE; i++) {
				if (buffer[i] > max) max = buffer[i];
			}
			printf("Max = '%c'\n", max);
		}
	}
	return 0;
}
