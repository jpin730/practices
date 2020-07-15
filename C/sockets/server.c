#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main (int argc, const char * argv[]) {
	if ( argc > 1 ) {
		int server_socket, client_socket, client_length, port;
		port = atoi(argv[1]);
		struct sockaddr_in server;
		struct sockaddr_in client;
		
		server.sin_family = AF_INET; // TCP/IP will be used
		server.sin_port =  htons(port); // host <s>hort to network
		server.sin_addr.s_addr = INADDR_ANY; // anyone can connect to server
		bzero( &(server.sin_zero), 8 ); // set 8 zeros in argument

		if ( ( server_socket = socket(AF_INET, SOCK_STREAM, 0) ) == -1 ) {
			printf("Socket cannot be opened.\n");
			return -1;
		}

		if ( bind( server_socket, (struct sockaddr *) &server, sizeof(struct sockaddr) ) == -1 ) {
			printf("Port %s cannot be opened.\n", argv[1]);
			return -2;
		}

		if ( listen( server_socket, 5 ) == -1 ) {
			printf("Cannot be listened.\n");
			return -3;
		}

		printf("Waiting clients...\n");

		client_length = sizeof(struct sockaddr_in);
		if (  (client_socket = accept( server_socket, (struct sockaddr *) &client, &client_length ) ) == -1 ) {
			printf("Connection was not accepted.\n");
			return -4;
		}

		char str[INET_ADDRSTRLEN];
		inet_ntop( AF_INET, &(client.sin_addr), str, INET_ADDRSTRLEN ); // client  networt to string

		printf("Client connected from %s,%d.\n", str, client.sin_port);
		send( client_socket, "Welcome to server.", 26, 0);

		printf("Message send.\n");
		shutdown(client_socket, 2); // how = 2: completely closed, no one can send/receive
		shutdown(server_socket, 2);
	} else {
		printf("Enter the port, please.\n");
		return -5;
	}
}
