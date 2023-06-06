#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks to see if list is a cycle
 * @list: linked list
 * Return: 0 for false, 1 true
 */

int check_cycle(listint_t *list)
{
	listint_t *copy;
	listint_t *location;
	unsigned int n;

	n = 0;
	copy = list;

	while (copy != NULL)
	{
		location = list;
		while (location != NULL)
		{
			if (location == copy)
				n++;
			location = location->next;
		}
		if (n > 1)
			return (1);
		n = 0;
	}
	return (0);
}
