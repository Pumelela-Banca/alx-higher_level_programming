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
	unsigned int b;

	copy = list;
	b = 0;

	while (copy != NULL)
	{
		location = list;
		while (location != NULL)
		{
			if (location == copy && location->next == copy->next)
				b++;
			location = location->next;
			if (b > 1)
				return (1);
		}
		copy = copy->next;
	}
	return (0);
}
