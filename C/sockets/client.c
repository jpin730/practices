#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main (int argc, const char * argv[]) {
	if ( argc > 2 ) {
		const char * ip;
		int client_socket, numbytes, port;
		char buffer[100];
		port = atoi(argv[2]);
		ip = argv[1];

		struct sockaddr_in server;

		if ( inet_pton(AF_INET, argv[1], &server.sin_addr) <= 0 ) { // ip to network
			printf("IP %s is not valid.\n", ip);
			return -1;
		}
		
		printf("Opening socket...\n");

		if ( (client_socket = socket( AF_INET, SOCK_STREAM, 0 )) == -1) {
			printf("Socket cannot be opened.\n");
			return -2;
		}

		server.sin_family = AF_INET;
		server.sin_port = htons(port);
		bzero( &(server.sin_zero), 8 );

		printf("Connecting to %s:%s...\n", argv[1], argv[2]);

		if ( connect( client_socket, (struct sockaddr *) &server, sizeof(struct sockaddr) ) == -1 ) {
			printf("Cannot connect to server.\n");
			return -3;
		}

		if ( ( numbytes = recv(client_socket, buffer, 100, 0 ) )  == -1) {
			printf("Error in read.\n");
			return -4;
		}

		buffer[numbytes] = '\0';

		printf("Server message: '%s' \n", buffer);

		shutdown(client_socket, 2);

	} else {
		printf("Enter the server ip and server port, please.\n");
		return -5;
	}
}
