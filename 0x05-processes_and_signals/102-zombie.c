#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>

/**
 * infinite_while - infinite loop
 *
 * Return: 0 on success
 */

int infinite_while(void)
{
	while (1)
		sleep(1);
	return (0);
}

/**
 * main - create 5 zombie processes
 *
 * Return: 0 always
 */

int main(void)
{
	int i, pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}
	infinite_while();
	return (0);
}
